from data_monitor.data_monitor import DataMonitor
from lap_viewer.lap_viewer import LapViewer
from PyQt5.QtWidgets import QApplication
import sys


class AppController:
    def __init__(self):
        super(AppController, self).__init__()
        self.app = QApplication(sys.argv)
        self.data_monitor = None
        self.lap_viewer = None

    # Starts the application by starting the monitor
    def start_app(self):
        self.data_monitor = DataMonitor(database_viewer_initializer=self.start_database_viewer)
        self.data_monitor.start()
        self.app.exec_()

    # Starts the database viewer thread
    # If one is created while one is running, the opened one is closed and a new one is created
    def start_database_viewer(self):
        self.lap_viewer = LapViewer()
        self.lap_viewer.start()


