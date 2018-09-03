from PyQt5.QtCore import QObject, pyqtSlot
from GUI.GUI_interface import GUIInterface
from actions.load_laps_action import LoadLapsAction
from actions.view_lap_action import ViewLapAction
from actions.create_table_action import CreateTableAction
from actions.plot_graph_action import PlotGraphAction
from definitions import DatabaseTableTypes, MonitoredItems
from models.laps.lap import Lap
from typing import Dict


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
        self.gui_interface.connect_plot_signal(self.plot_handler)

    @pyqtSlot(int)
    def view_lap_handler(self, lap_id: int) -> None:
        ViewLapAction(self, lap_id=lap_id).execute()

    @pyqtSlot(DatabaseTableTypes)
    def table_selected_handler(self, table_type: DatabaseTableTypes):
        CreateTableAction(self, table_type=table_type).execute()

    @pyqtSlot(object)  # Can't use dict or Dict with PyQt5
    def plot_handler(self, items_to_plot: Dict[MonitoredItems, bool]):
        PlotGraphAction(self, items_to_plot=items_to_plot).execute()
