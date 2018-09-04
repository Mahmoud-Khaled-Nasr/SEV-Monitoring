from PyQt5.QtCore import QObject, pyqtSlot

from monitoring.GUI.GUI_interface import GUIInterface
from monitoring.input.serial_reader import SerialReader
from models.data_frames.data_frame import DataFrame
from models.laps.lap import Lap
from definitions import ConnectionTypes

from monitoring.actions.start_action import StartAction
from monitoring.actions.receive_new_data_frame_action import ReceiveNewDataFrameAction
from monitoring.actions.stop_action import StopAction


class Dispatcher(QObject):

    def __init__(self, gui_interface: GUIInterface, serial_reader: SerialReader):
        super(Dispatcher, self).__init__()
        self.gui_interface: GUIInterface = gui_interface
        self.__connect_gui_signals()
        self.serial_reader: SerialReader = serial_reader
        self.__connect_serial_reader_signals()
        self.current_lap: Lap = None

    # Private method: Connects gui signals to their slots
    def __connect_gui_signals(self) -> None:
        self.gui_interface.connect_start_signal(self.start_handler)
        self.gui_interface.connect_stop_signal(self.stop_handler)

    # Private method: Connect serial input signals to their slots
    def __connect_serial_reader_signals(self) -> None:
        self.serial_reader.connect_receive_data_signal(self.receive_serial_data_handler)

    @pyqtSlot(DataFrame)
    def receive_serial_data_handler(self, data_frame: DataFrame) -> None:
        ReceiveNewDataFrameAction(self, data_frame).execute()

    @pyqtSlot(ConnectionTypes, str)  # Connection type and lap name
    def start_handler(self, connection_type: ConnectionTypes, lap_name: str):
        StartAction(self, connection_type, lap_name).execute()

    @pyqtSlot()
    def stop_handler(self):
        StopAction(self).execute()
