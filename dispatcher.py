from PyQt5.QtCore import QObject, pyqtSlot

from GUI.GUI_interface import GUIInterface
from input.input import SerialInterface
from models.data_frames.data_frame import DataFrame
from models.laps.lap import Lap
from database import Session
from definitions import ConnectionTypes


class Dispatcher(QObject):

    def __init__(self, gui_interface: GUIInterface, serial_interface: SerialInterface, database_session: Session):
        super(Dispatcher, self).__init__()
        self.gui_interface: GUIInterface = gui_interface
        self.make_gui_connections()
        self.serial_interface: SerialInterface = serial_interface
        self.make_serial_interface_connections()
        self.database_session: Session = database_session
        self.current_lap: Lap = None

    # Connects gui signals to their slots
    def make_gui_connections(self) -> None:
        self.gui_interface.gui_actions.signal_start.connect(self.start_handler)
        self.gui_interface.gui_actions.signal_stop.connect(self.stop_handler)

    # Connect serial input signals to their slots
    def make_serial_interface_connections(self) -> None:
        self.serial_interface.signal_receive_serial_data.connect(self.receive_serial_data_handler)

    @pyqtSlot(DataFrame)
    def receive_serial_data_handler(self, data_frame: DataFrame) -> None:
        pass

    @pyqtSlot(ConnectionTypes)   
    def start_handler(self):
        pass

    @pyqtSlot()
    def stop_handler(self):
        pass
