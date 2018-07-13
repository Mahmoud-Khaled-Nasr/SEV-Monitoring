from PyQt5.QtCore import QObject, pyqtSlot

from GUI.GUI_Interface import GUIApp
from input.input import SerialInterface
from models.data_frames.data_frame import DataFrame
from models.laps.lap import Lap
from database import Session


class Dispatcher(QObject):

    def __init__(self, gui_interface: GUIApp, serial_interface: SerialInterface, database_session: Session):
        super(Dispatcher, self).__init__()
        self.gui_interface: GUIApp = gui_interface
        self.make_gui_connections()
        self.serial_interface: SerialInterface = serial_interface
        self.make_serial_interface_connections()
        self.database_session: Session = database_session
        self.current_lap: Lap = None

    def make_gui_connections(self) -> None:
        pass
        # here we assign the proper function to each signal

    def make_serial_interface_connections(self) -> None:
        self.serial_interface.signal_receive_serial_data.connect(self.receive_serial_data_handler)

    @pyqtSlot(DataFrame)
    def receive_serial_data_handler(self, data_frame: DataFrame) -> None:
        pass
