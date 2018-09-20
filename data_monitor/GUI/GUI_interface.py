from data_monitor.GUI.GUI_main_window import MainWindow
from data_monitor.GUI.GUI_actions import GUIActions, GUIUpdater
from typing import List, Callable
import sys


class GUIInterface:

    # Constructor
    def __init__(self):
        # Initializations
        self.gui_app = MainWindow()
        self.gui_updater = GUIUpdater(self.gui_app)
        self.gui_actions = GUIActions(self.gui_app, self.gui_updater)

        # Testing
        self.update_currents(30.5, 15.1, 150.312341)
        self.update_currents(310, 50, 250)
        self.update_currents(100, 50, 250.5)
        self.update_lights([True, False, True])
        self.update_switches([False, True, False, True, True, False])

    # Shows the main window
    def start_gui(self) -> None:
        self.gui_app.main_window.showMaximized()

    # Updates the currents on the GUI
    def update_currents(self, battery_current: float, motors_current: float, solar_panels_current: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.batteryCurrent, battery_current)
        self.gui_updater.update_label(self.gui_app.motorsCurrent, motors_current)
        self.gui_updater.update_label(self.gui_app.spanelsCurrent, solar_panels_current)

    # Updates the voltages on the GUI
    def update_volts(self, dc_bus_volt: float, charge_rate: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.dcBusVolt, dc_bus_volt)
        self.gui_updater.update_label(self.gui_app.chargeRate, charge_rate)

    # Updates the temperatures on the GUI
    def update_temperatures(self,solar_panels_temperature: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.spanelsTemp, solar_panels_temperature)

    # Updates the Master Motor Data on the GUI
    def update_master_motor(self, master_motor_current: float, master_motor_speed: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.masterCurrent, master_motor_current)
        self.gui_updater.update_label(self.gui_app.masterSpeed, master_motor_speed)

    # Updates the Slave Motor Data on the GUI
    def update_slave_motor(self, slave_motor_current: float, slave_motor_speed: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.slaveCurrent, slave_motor_current)
        self.gui_updater.update_label(self.gui_app.slaveSpeed, slave_motor_speed)

    # Updates the batteries data
    def update_battery(self, module_number: int, battery_volt: float, battery_temperature: float) -> None:
        self.gui_updater.update_battery(module_number, battery_volt, battery_temperature)

    # Updates lights status in the GUI
    def update_lights(self, lights_status: List[bool]) -> None:
        self.gui_updater.update_lights(lights_status)

    # Updates switches status in the GUI
    def update_switches(self, switches_status: List[bool]) -> None:
        self.gui_updater.update_switches(switches_status)

    # Connects the start signal to its slot
    def connect_start_signal(self, start_slot: Callable) -> None:
        self.gui_actions.signal_start.connect(start_slot)

    # Connects the stop signal to its slot
    def connect_stop_signal(self, stop_slot: Callable) -> None:
        self.gui_actions.signal_stop.connect(stop_slot)

    # Connects the view laps signal to its slot
    def connect_view_laps_signal(self, view_laps_slot: Callable) -> None:
        self.gui_actions.signal_view_laps.connect(view_laps_slot)