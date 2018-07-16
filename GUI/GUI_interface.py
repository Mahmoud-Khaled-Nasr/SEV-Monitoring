from GUI.GUI_main_window import MainWindow
from GUI.GUI_actions import GUIActions, GUIUpdater
from typing import List
import sys


class GUIInterface:

    # Constructor
    def __init__(self):
        # Initializations
        self.gui_app = MainWindow()
        self.gui_updater = GUIUpdater(self.gui_app)
        self.gui_actions = GUIActions(self.gui_app, self.gui_updater)
        # Initialize signals
        self.signal_start = self.gui_actions.signal_start
        self.signal_stop = self.gui_actions.signal_stop

        # Testing
        self.update_currents(30.5, 15.1, 150.312341)
        self.update_currents(310, 50, 250)
        self.update_currents(100, 50, 250.5)
        self.update_lights([True, False, True])

    def start_gui(self) -> None:
        # Start the main event loop
        sys.exit(self.gui_app.app.exec_())

    # Updates the currents on the GUI
    def update_currents(self, battery_current: float, motors_current: float, solar_panels_current: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.batteryCurrent, battery_current)
        self.gui_updater.update_label(self.gui_app.motorsCurrent, motors_current)
        self.gui_updater.update_label(self.gui_app.spanelsCurrent, solar_panels_current)

    # Updates the voltages on the GUI
    def update_volts(self, dc_bus_volt: float, xVolt: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.dcBusVolt, dc_bus_volt)
        self.gui_updater.update_label(self.gui_app.xVolt, xVolt)

    # Updates the temperatures on the GUI
    def update_temperatures(self, xTemp: float, solar_panels_temperature: float, yTemp: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.xTemp, xTemp)
        self.gui_updater.update_label(self.gui_app.spanelsTemp, solar_panels_temperature)
        self.gui_updater.update_label(self.gui_app.yTemp, yTemp)

    # Updates the Master Motor MC Data on the GUI
    def update_master_mc(self, master_current: float, master_speed: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.masterCurrent, master_current)
        self.gui_updater.update_label(self.gui_app.masterSpeed, master_speed)

    # Updates the Slave Motor MC Data on the GUI
    def update_slave_mc(self, slave_current: float, slave_speed: float) -> None:
        # Updates the labels with the given values
        self.gui_updater.update_label(self.gui_app.slaveCurrent, slave_current)
        self.gui_updater.update_label(self.gui_app.slaveSpeed, slave_speed)

    # Updates the batteries data
    def update_batteries(self, batteries_volts: List[float], batteries_temps: List[float]) -> None:
        self.gui_updater.update_batteries(batteries_volts, batteries_temps)

    # Updates lights status in the GUI
    def update_lights(self, lights_status: List[bool]) -> None:
        self.gui_updater.update_lights(lights_status)

    # Updates switches status in the GUI
    def update_switches(self, switches_status: List[bool]) -> None:
        self.gui_updater.update_switches(switches_status)