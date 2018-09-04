from database_viewing.GUI.GUI_main_window import MainWindow
from database_viewing.GUI.GUI_actions import GUIActions
import sys
from typing import Callable


class GUIInterface:
    # Constructor
    def __init__(self):  # Parameter for testing
        # Initializations
        self.gui_app = MainWindow()
        self.gui_actions = GUIActions(self.gui_app)

    # Starts the main event loop
    def start_gui(self) -> None:
        # Start the main event loop
        sys.exit(self.gui_app.app.exec_())

    # Creates a new list item and adds it to the laps list
    def update_laps_list(self, laps) -> None:
        self.gui_actions.update_laps_list(laps)

    # Updates the table data
    def update_table_data(self, column_count: int, table_data, table_column_headers):
        self.gui_actions.update_table_data(column_count=column_count,
                                           table_data=table_data,
                                           table_column_headers=table_column_headers)

    # Plots the given data on the graph canvas
    def plot(self, all_graphs_data):
        self.gui_actions.plot(all_graphs_data=all_graphs_data)

    # Connects the view lap signal to its slot
    def connect_view_lap_signal(self, view_lap_slot: Callable):
        self.gui_actions.signal_view_lap.connect(view_lap_slot)

    # Connects the table selected signal to its slot
    def connect_table_selected_signal(self, table_selected_slot: Callable):
        self.gui_actions.signal_table_selected.connect(table_selected_slot)

    def connect_plot_signal(self, plot_slot: Callable):
        self.gui_actions.signal_plot.connect(plot_slot)
