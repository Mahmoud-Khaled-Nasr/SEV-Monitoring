from GUI.GUI_main_window import Ui_MainWindow
from GUI.GUI_lap_widget import LapWidget
from PyQt5.QtCore import pyqtSignal, QObject
from definitions import DatabaseTableTypes, MonitoredItems
from typing import Dict


class GUIActions(QObject):
    # Signals
    signal_view_lap = pyqtSignal(int)
    signal_table_selected = pyqtSignal(DatabaseTableTypes)
    signal_plot = pyqtSignal(object)  # Can't use dict or Dict with PyQt5

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
        self.gui_app.plotButton.clicked.connect(self.plot_button_pressed)

    def view_lap_button_pressed(self) -> None:
        # Get the lap id from the selected lap widget
        laps_list = self.gui_app.lapsList
        lap_widget: LapWidget = laps_list.itemWidget(laps_list.currentItem())
        # Do nothing if no lap is selected
        if lap_widget is None:
            return
        lap_id = lap_widget.lap_id
        # Emit a signal
        self.signal_view_lap.emit(lap_id)
        print("view lap signal emitted with lap id " + str(lap_id))
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

    def plot_button_pressed(self) -> None:
        checked_items: Dict[MonitoredItems, bool] = {}
        # Initialize the dictionary
        for item in MonitoredItems:
            checked_items[item] = False
        # Check for checked items
        # Battery Current
        if self.gui_app.checkbox_batteryCurrent.isChecked():
            checked_items[MonitoredItems.BATTERY_CURRENT] = True
        # Motor Current
        if self.gui_app.checkbox_motorCurrent.isChecked():
            checked_items[MonitoredItems.MOTORS_CURRENT] = True
        # Solar Panels Current
        if self.gui_app.checkbox_solarPanelsCurrent.isChecked():
            checked_items[MonitoredItems.SOLAR_PANELS_CURRENT] = True
        # Solar Panels Temperature
        if self.gui_app.checkbox_solarPanelsTemperature.isChecked():
            checked_items[MonitoredItems.SOLAR_PANELS_TEMPERATURE] = True
        # DC Bus Voltage
        if self.gui_app.checkbox_DCBusVoltage.isChecked():
            checked_items[MonitoredItems.DC_BUS_VOLT] = True
        # Charge Rate
        if self.gui_app.checkbox_chargeRate.isChecked():
            checked_items[MonitoredItems.CHARGE_RATE] = True
        # Min Battery Voltage
        if self.gui_app.checkbox_minBatteryVoltage.isChecked():
            checked_items[MonitoredItems.MIN_BATTERY_VOLT] = True
        # Max Battery Voltage
        if self.gui_app.checkbox_maxBatteryVoltage.isChecked():
            checked_items[MonitoredItems.MAX_BATTERY_VOLT] = True
        # Max Battery Temperature
        if self.gui_app.checkbox_maxBatteryTemperature.isChecked():
            checked_items[MonitoredItems.MAX_BATTERY_TEMPERATURE] = True
        # Master Motor Current
        if self.gui_app.checkbox_masterMotorCurrent.isChecked():
            checked_items[MonitoredItems.MASTER_MOTOR_CURRENT] = True
        # Master Motor Speed
        if self.gui_app.checkbox_masterMotorSpeed.isChecked():
            checked_items[MonitoredItems.MASTER_MOTOR_SPEED] = True
        # Slave Motor Current
        if self.gui_app.checkbox_slaveMotorCurrent.isChecked():
            checked_items[MonitoredItems.SLAVE_MOTOR_CURRENT] = True
        # Slave Motor Speed
        if self.gui_app.checkbox_slaveMotorSpeed.isChecked():
            checked_items[MonitoredItems.SLAVE_MOTOR_SPEED] = True

        # Emit a signal
        self.signal_plot.emit(checked_items)
