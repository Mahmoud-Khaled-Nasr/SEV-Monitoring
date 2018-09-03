from GUI.GUI_main_window import MainWindow
from GUI.GUI_actions import GUIActions
from GUI.GUI_lap_widget import LapWidget
from PyQt5.QtWidgets import QListWidgetItem, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QFont
import sys
from typing import Callable, List


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
        for lap in laps:
            # Create lap widget
            lap_widget = LapWidget(lap_name= lap.name, lap_id= lap.id)
            # Add the lap to the list
            # Create a list widget item
            list_widget_item = QListWidgetItem()
            list_widget_item.setSizeHint(lap_widget.sizeHint())
            # Add the list widget item to the list
            self.gui_app.lapsList.addItem(list_widget_item)
            # Set the list widget item to the lap widget
            self.gui_app.lapsList.setItemWidget(list_widget_item, lap_widget)

    # Updates the table data
    def update_table_data(self, column_count: int, table_data, table_column_headers):
        # Create the table
        table: QTableWidget = self.gui_app.tableWidget
        table_font = QFont()
        table_font.setPointSize(12)
        table.setFont(table_font)
        table.horizontalHeader().setFont(table_font)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Clear the table
        while table.columnCount() != 0:
            table.removeColumn(0)
        while table.rowCount() != 0:
            table.removeRow(0)
        # Insert new columns
        for index in range(0, column_count):
            table.insertColumn(index)
        # Set the headers
        table.setHorizontalHeaderLabels(table_column_headers)
        # Add row by row
        for row_data in table_data:
            row_number = table_data.index(row_data)
            table.insertRow(row_number)
            # Add items in the row, cell by cell
            for column_number in range(0, column_count):
                table.setItem(row_number, column_number, QTableWidgetItem(str(row_data[column_number])))

    # Plots the given data on the graph canvas
    def plot(self, all_graphs_data):
        # all_graphs_data: All data that needs to be plotted as a list of tuples, each tuple is a graph
        # Each tuple contains 2 lists, one for X values and one for Y values
        self.gui_app.graph_figure.clear()
        axes = self.gui_app.graph_figure.add_subplot(111)
        for graph_data in all_graphs_data:
            (x, y) = graph_data
            axes.plot(x,y)
        self.gui_app.graph_canvas.draw()

    # Connects the view lap signal to its slot
    def connect_view_lap_signal(self, view_lap_slot: Callable):
        self.gui_actions.signal_view_lap.connect(view_lap_slot)

    # Connects the table selected signal to its slot
    def connect_table_selected_signal(self, table_selected_slot: Callable):
        self.gui_actions.signal_table_selected.connect(table_selected_slot)

    def connect_plot_signal(self, plot_slot: Callable):
        self.gui_actions.signal_plot.connect(plot_slot)
