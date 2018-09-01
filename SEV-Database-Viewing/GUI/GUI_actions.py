from GUI.GUI_main_window import Ui_MainWindow
from GUI.GUI_lap_widget import LapWidget
from PyQt5.QtCore import pyqtSignal, QObject
from definitions import DatabaseTableTypes


class GUIActions(QObject):
    # Signals
    signal_view_lap = pyqtSignal(int)
    signal_table_selected = pyqtSignal(DatabaseTableTypes)

    # Constructor
    def __init__(self, gui_app: Ui_MainWindow):
        super(GUIActions, self).__init__()
        # Initializations
        self.gui_app = gui_app
        # Connect button press signals
        self.__set_buttons_connections()

    # Private method: Connects the buttons clicks to their action
    def __set_buttons_connections(self) -> None:
        self.gui_app.viewLabButton.clicked.connect(self.view_lap_button_pressed)
        self.gui_app.tableSelector.currentIndexChanged.connect(self.table_selector_changed)

    def view_lap_button_pressed(self) -> None:
        # Get the lap id from the selected lap widget
        laps_list = self.gui_app.lapsList
        lap_widget: LapWidget = laps_list.itemWidget(laps_list.currentItem())
        # Do nothing if no lap is selected
        if lap_widget is None:
            return
        lap_id = lap_widget.lap_id
        # Emit a signal
        print(lap_id)
        self.signal_view_lap.emit(lap_id)
        print("signal emitted with lap id " + str(lap_id))
        # Remove the lap selector widget
        self.gui_app.stackedWidget.removeWidget(self.gui_app.stackedWidget.currentWidget())

    def table_selector_changed(self, table_index: int) -> None:
        # Currents table
        if table_index == 0:
            self.signal_table_selected.emit(DatabaseTableTypes.CURRENTS_TABLE)
        # Bus Voltages table
        elif table_index == 1:
            self.signal_table_selected.emit(DatabaseTableTypes.BUS_VOLTAGES_TABLE)
        # Temperatures table
        elif table_index == 2:
            self.signal_table_selected.emit(DatabaseTableTypes.TEMPERATURES_TABLE)
        # Batteries table
        elif table_index == 3:
            self.signal_table_selected.emit(DatabaseTableTypes.BATTERIES_TABLE)
        # Master Motor table
        elif table_index == 4:
            self.signal_table_selected.emit(DatabaseTableTypes.MASTER_MOTOR_TABLE)
        # Slave Motor table
        elif table_index == 5:
            self.signal_table_selected.emit(DatabaseTableTypes.SLAVE_MOTOR_TABLE)
        # Lights table
        elif table_index == 6:
            self.signal_table_selected.emit(DatabaseTableTypes.LIGHTS_TABLE)
        # Switches table
        elif table_index == 7:
            self.signal_table_selected.emit(DatabaseTableTypes.SWITCHES_TABLE)

