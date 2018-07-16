from PyQt5.QtCore import QObject, pyqtSlot

from GUI.GUI_interface import GUIInterface
from input.serial_reader import SerialReader
from models.data_frames.data_frame import DataFrame
from models.laps.lap import Lap
from database import Session
from definitions import ConnectionTypes

from actions.start_action import StartAction
from actions.receive_new_data_frame_action import ReceiveNewDataFrameAction
from actions.stop_action import StopAction


class Dispatcher(QObject):

    def __init__(self, gui_interface: GUIInterface, serial_reader: SerialReader, database_session: Session):
        super(Dispatcher, self).__init__()
        self.gui_interface: GUIInterface = gui_interface
        self.connect_gui_signals()
        self.serial_reader: SerialReader = serial_reader
        self.connect_serial_reader_signals()
        self.database_session: Session = database_session
        self.current_lap: Lap = None

    # Connects gui signals to their slots
    def connect_gui_signals(self) -> None:
        self.gui_interface.connect_start_signal(self.start_handler)
        self.gui_interface.connect_stop_signal(self.stop_handler)

    # Connect serial input signals to their slots
    def connect_serial_reader_signals(self) -> None:
        self.serial_reader.connect_receive_data_signal(self.receive_serial_data_handler)

    @pyqtSlot(DataFrame)
    def receive_serial_data_handler(self, data_frame: DataFrame) -> None:
        ReceiveNewDataFrameAction(self, data_frame).execute()

    @pyqtSlot(ConnectionTypes)   
    def start_handler(self):
        StartAction(self).execute()

    @pyqtSlot()
    def stop_handler(self):
        StopAction(self).execute()
