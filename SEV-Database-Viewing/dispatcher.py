from PyQt5.QtCore import QObject, pyqtSlot
from GUI.GUI_interface import GUIInterface
from actions.load_laps_action import LoadLapsAction
from actions.view_lap_action import ViewLapAction
from actions.create_table_action import CreateTableAction
from definitions import DatabaseTableTypes
from models.laps.lap import Lap


class Dispatcher(QObject):
    # Constructor
    def __init__(self, gui_interface: GUIInterface):
        super(Dispatcher, self).__init__()
        self.gui_interface: GUIInterface = gui_interface
        self.__connect_signals()
        self.current_lap: Lap = None
        # Load the laps to the GUI
        LoadLapsAction(self).execute()

    # Connect signals to slots
    def __connect_signals(self):
        self.gui_interface.connect_view_lap_signal(self.view_lap_handler)
        self.gui_interface.connect_table_selected_signal(self.table_selected_handler)

    @pyqtSlot(int)
    def view_lap_handler(self, lap_id: int) -> None:
        ViewLapAction(self, lap_id).execute()

    @pyqtSlot(DatabaseTableTypes)
    def table_selected_handler(self, table_type: DatabaseTableTypes):
        CreateTableAction(self, table_type).execute()