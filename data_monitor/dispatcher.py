from PyQt5.QtCore import QObject, pyqtSlot
from typing import Callable

from data_monitor.GUI.GUI_interface import GUIInterface
from data_monitor.input.serial_reader import SerialReader
from models.data_frames.data_frame import DataFrame
from models.laps.lap import Lap
from definitions import ConnectionTypes

from data_monitor.actions.start_action import StartAction
from data_monitor.actions.receive_new_data_frame_action import ReceiveNewDataFrameAction
from data_monitor.actions.stop_action import StopAction
from data_monitor.actions.view_laps_action import ViewLapsAction


class Dispatcher(QObject):

    def __init__(self, gui_interface: GUIInterface, serial_reader: SerialReader):
        super(Dispatcher, self).__init__()
        self.gui_interface: GUIInterface = gui_interface
        self.__connect_gui_signals()
        self.serial_reader: SerialReader = serial_reader
        self.__connect_serial_reader_signals()
        self.current_lap: Lap = None

    # Starts the monitoring GUI
    def start_gui(self):
        self.gui_interface.start_gui()

    # Private method: Connects gui signals to their slots
    def __connect_gui_signals(self) -> None:
        self.gui_interface.connect_start_signal(self.start_handler)
        self.gui_interface.connect_stop_signal(self.stop_handler)

    # Private method: Connect serial input signals to their slots
    def __connect_serial_reader_signals(self) -> None:
        self.serial_reader.connect_receive_data_signal(self.receive_serial_data_handler)

    # Connects the view laps signal to an external slot
    def connect_view_laps_signal(self, view_laps_handler: Callable):
        self.gui_interface.connect_view_laps_signal(view_laps_handler)

    @pyqtSlot(DataFrame)
    def receive_serial_data_handler(self, data_frame: DataFrame) -> None:
        ReceiveNewDataFrameAction(self, data_frame).execute()

    @pyqtSlot(ConnectionTypes, str)  # Connection type and lap name
    def start_handler(self, connection_type: ConnectionTypes, lap_name: str):
        StartAction(self, connection_type, lap_name).execute()

    @pyqtSlot()
    def stop_handler(self):
        StopAction(self).execute()
