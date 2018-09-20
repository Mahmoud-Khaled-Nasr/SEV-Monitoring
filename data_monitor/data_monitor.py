from data_monitor.dispatcher import Dispatcher
from data_monitor.GUI.GUI_interface import GUIInterface
from data_monitor.input.serial_reader import SerialReader
from typing import Callable
from PyQt5.QtCore import pyqtSlot, QObject

COM_PORT = "COM7"
BAUD_RATE = 9600


class DataMonitor(QObject):

    def __init__(self, database_viewer_initializer: Callable):
        super(DataMonitor, self).__init__()
        self.database_viewer_initializer = database_viewer_initializer
        gui_interface = GUIInterface()
        serial_reader = SerialReader(COM_PORT, BAUD_RATE)
        self.dispatcher = Dispatcher(gui_interface=gui_interface, serial_reader=serial_reader)
        self.dispatcher.connect_view_laps_signal(view_laps_handler=self.start_database_viewer)

    def start(self):
        self.dispatcher.gui_interface.start_gui()

    @pyqtSlot()
    def start_database_viewer(self):
        self.database_viewer_initializer()


