from PyQt5.QtCore import QObject, pyqtSlot
from database_viewing.GUI.GUI_interface import GUIInterface
from database_viewing.actions.load_laps_action import LoadLapsAction
from database_viewing.actions.view_lap_action import ViewLapAction
from database_viewing.actions.create_table_action import CreateTableAction
from database_viewing.actions.plot_graph_action import PlotGraphAction
from database_viewing.actions.delete_lap_action import DeleteLapAction
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

    # Connect signals to their slots
    def __connect_signals(self) -> None:
        self.gui_interface.connect_view_lap_signal(self.view_lap_handler)
        self.gui_interface.connect_table_selected_signal(self.table_selected_handler)
        self.gui_interface.connect_plot_signal(self.plot_handler)
        self.gui_interface.connect_delete_lap_signal(self.delete_lap_handler)

    @pyqtSlot(int)
    def view_lap_handler(self, lap_id: int) -> None:
        ViewLapAction(self, lap_id=lap_id).execute()

    @pyqtSlot(DatabaseTableTypes)
    def table_selected_handler(self, table_type: DatabaseTableTypes) -> None:
        CreateTableAction(self, table_type=table_type).execute()

    @pyqtSlot(object)  # Can't use dict or Dict with PyQt5, so object is used instead
    def plot_handler(self, items_to_plot: Dict[MonitoredItems, bool]) -> None:
        PlotGraphAction(self, items_to_plot=items_to_plot).execute()

    @pyqtSlot(int)
    def delete_lap_handler(self, lap_id: int) -> None:
        DeleteLapAction(self, lap_id=lap_id).execute()