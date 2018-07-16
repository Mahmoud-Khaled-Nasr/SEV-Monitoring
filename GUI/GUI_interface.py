from GUI.GUI_main_window import MainWindow
from GUI.GUI_actions import GUIActions
from PyQt5.QtWidgets import QLabel
from definitions import Ranges, Tolerances
from typing import List
import sys


class GUIInterface:

    # Constructor
    def __init__(self):
        # Create a main GUI
        self.gui_app = MainWindow()
        # Create a GUI Actions object
        self.gui_actions = GUIActions(self.gui_app)
        # Set paused flag as false
        self.paused = False
        # Connect buttons to actions
        self.__set_button_connections()
        # Create needed dictionaries
        self.ranges = {}
        self.tolerances = {}
        self.recent_values = {}
        # Initialize the dictionaries
        self.__init_ranges_dict()
        self.__init_tolerances_dict()

        # Testing
        self.update_currents(30.5, 15.1, 150.312341)
        self.update_currents(310, 50, 250)
        self.update_currents(100, 50, 250.5)
        self.update_lights([True, False, True])

    def start_gui(self) -> None:
        # Start the main event loop
        sys.exit(self.gui_app.app.exec_())

    # Private method: Connects the buttons clicks to their action
    def __set_button_connections(self) -> None:
        self.gui_app.start_stop_button.clicked.connect(self.gui_actions.start_stop_button_clicked)
        self.gui_app.pause_continue_button.clicked.connect(self.gui_actions.pause_continue_button_clicked)
        self.gui_actions.signal_pause.connect(self.set_paused)

    # Private method: Initializes the ranges dictionary
    def __init_ranges_dict(self) -> None:
        # Currents
        self.ranges[self.gui_app.batteryCurrent] = Ranges.battery_current
        self.ranges[self.gui_app.motorsCurrent] = Ranges.motors_current
        self.ranges[self.gui_app.spanelsCurrent] = Ranges.solar_panels_current
        # Temperatures
        self.ranges[self.gui_app.xTemp] = Ranges.x_temperature
        self.ranges[self.gui_app.yTemp] = Ranges.y_temperature
        self.ranges[self.gui_app.spanelsTemp] = Ranges.solar_panels_temperature
        # Battery Data
        self.ranges[self.gui_app.minBatteryVolt] = Ranges.min_battery_volt
        self.ranges[self.gui_app.maxBatteryVolt] = Ranges.max_battery_volt
        self.ranges[self.gui_app.maxBatteryTemp] = Ranges.max_battery_temperature
        # Voltages
        self.ranges[self.gui_app.xVolt] = Ranges.x_volt
        self.ranges[self.gui_app.dcBusVolt] = Ranges.dc_bus_volt
        # Master Motor
        self.ranges[self.gui_app.masterCurrent] = Ranges.master_motor_current
        self.ranges[self.gui_app.masterSpeed] = Ranges.master_motor_speed
        # Slave Motor
        self.ranges[self.gui_app.slaveCurrent] = Ranges.slave_motor_current
        self.ranges[self.gui_app.slaveSpeed] = Ranges.slave_motor_speed
        # Battery Modules
        for i in range(1, 15):
            self.ranges[eval("self.gui_app.batteryVolt" + str(i))] = Ranges.battery_module_volt
            self.ranges[eval("self.gui_app.batteryTemp" + str(i))] = Ranges.battery_module_temperature

    # Private method: Initializes the tolerances dictionary
    def __init_tolerances_dict(self) -> None:
        # Currents
        self.tolerances[self.gui_app.batteryCurrent] = Tolerances.battery_current
        self.tolerances[self.gui_app.motorsCurrent] = Tolerances.motors_current
        self.tolerances[self.gui_app.spanelsCurrent] = Tolerances.solar_panels_current
        # Temperatures
        self.tolerances[self.gui_app.xTemp] = Tolerances.x_temperature
        self.tolerances[self.gui_app.yTemp] = Tolerances.y_temperature
        self.tolerances[self.gui_app.spanelsTemp] = Tolerances.solar_panels_temperature
        # Battery Data
        self.tolerances[self.gui_app.minBatteryVolt] = Tolerances.min_battery_volt
        self.tolerances[self.gui_app.maxBatteryVolt] = Tolerances.max_battery_volt
        self.tolerances[self.gui_app.maxBatteryTemp] = Tolerances.max_battery_temperature
        # Voltages
        self.tolerances[self.gui_app.xVolt] = Tolerances.x_volt
        self.tolerances[self.gui_app.dcBusVolt] = Tolerances.dc_bus_volt
        # Master Motor
        self.tolerances[self.gui_app.masterCurrent] = Tolerances.master_motor_current
        self.tolerances[self.gui_app.masterSpeed] = Tolerances.master_motor_speed
        # Slave Motor
        self.tolerances[self.gui_app.slaveCurrent] = Tolerances.slave_motor_current
        self.tolerances[self.gui_app.slaveSpeed] = Tolerances.slave_motor_speed
        # Battery Modules
        for i in range(1, 15):
            self.tolerances[eval("self.gui_app.batteryVolt" + str(i))] = Tolerances.battery_module_volt
            self.tolerances[eval("self.gui_app.batteryTemp" + str(i))] = Tolerances.battery_module_temperature

    # Checks if a value is in range for a certain type of data
    def __is_in_range(self, data_label: QLabel, value: float) -> bool:
        (minimum, maximum) = self.ranges[data_label]
        if minimum <= value <= maximum:
            return True
        else:
            return False

    # Checks if the change in value is tolerable
    def __is_tolerable(self, data_label: QLabel, value: float) -> bool:
        # No existing value yet, not tolerable
        if data_label not in self.recent_values:
            return False
        # The difference magnitude is below the tolerance
        elif abs(value - self.recent_values[data_label]) < self.tolerances[data_label]:
            return True
        else:
            return False

    # Updates the label with the value
    def __update_label(self, data_label: QLabel, value: float) -> None:
        # Check if the change in value is not tolerable
        if not self.__is_tolerable(data_label, value):
            # Update the recent value
            self.recent_values[data_label] = value
            if not self.paused:
                # Convert the passed floats to strings with precision 2 dp
                # then set it as text for the output label
                data_label.setText("{:.2f}".format(value))
                # Default stylesheets for labels and their frames
                stylesheet = "color: black;"
                parent_frame = data_label.parent().objectName()
                frame_stylesheet = "QFrame#" + parent_frame + "{border: 1px solid #828790;}"
                # Check if it is out of range
                if not self.__is_in_range(data_label, value):
                    #  Out-of-range stylesheets
                    stylesheet = "color: #dd0000;"
                    frame_stylesheet = "QFrame#" + parent_frame + "{border: 1px solid #dd0000;}"
                # Set stylesheets
                data_label.setStyleSheet(stylesheet)
                data_label.parent().setStyleSheet(frame_stylesheet)

    # Sets the paused flag (slot for the pause signal)
    def set_paused(self, is_paused: bool) -> None:
        self.paused = is_paused

    # Updates the currents on the GUI
    def update_currents(self, battery_current: float, motors_current: float, solar_panels_current: float) -> None:
        # Updates the labels with the given values
        self.__update_label(self.gui_app.batteryCurrent, battery_current)
        self.__update_label(self.gui_app.motorsCurrent, motors_current)
        self.__update_label(self.gui_app.spanelsCurrent, solar_panels_current)

    # Updates the voltages on the GUI
    def update_volts(self, dc_bus_volt: float, xVolt: float) -> None:
        # Updates the labels with the given values
        self.__update_label(self.gui_app.dcBusVolt, dc_bus_volt)
        self.__update_label(self.gui_app.xVolt, xVolt)

    # Updates the temperatures on the GUI
    def update_temperatures(self, xTemp: float, solar_panels_temperature: float, yTemp: float) -> None:
        # Updates the labels with the given values
        self.__update_label(self.gui_app.xTemp, xTemp)
        self.__update_label(self.gui_app.spanelsTemp, solar_panels_temperature)
        self.__update_label(self.gui_app.yTemp, yTemp)

    # Updates the Master Motor MC Data on the GUI
    def update_master_mc(self, master_current: float, master_speed: float) -> None:
        # Updates the labels with the given values
        self.__update_label(self.gui_app.masterCurrent, master_current)
        self.__update_label(self.gui_app.masterSpeed, master_speed)

    # Updates the Slave Motor MC Data on the GUI
    def update_slave_mc(self, slave_current: float, slave_speed: float) -> None:
        # Updates the labels with the given values
        self.__update_label(self.gui_app.slaveCurrent, slave_current)
        self.__update_label(self.gui_app.slaveSpeed, slave_speed)

    # Updates the batteries data on the GUI
    def update_batteries_data(self, batteries_volts: List[float], batteries_temps: List[float]) -> None:
        # index is an enumeration, starting at 1
        # volt and temp are elements in batteryVolts and batteryTemps respectively
        # eval is used to obtain the right label object through its name
        for index, (volt, temp) in enumerate(zip(batteries_volts, batteries_temps), 1):
            # Get volt label
            volt_label = eval("self.gui_app.batteryVolt" + str(index))
            # Get temperature label
            temp_label = eval("self.gui_app.batteryTemp" + str(index))

            # Updates the labels with the given values
            self.__update_label(volt_label, volt)
            self.__update_label(temp_label, temp)

        # Set the highlights
        max_volt = max(batteries_volts)
        min_volt = min(batteries_volts)
        max_temp = max(batteries_temps)

        # Updates the labels with the given values
        self.__update_label(self.gui_app.minBatteryVolt, min_volt)
        self.__update_label(self.gui_app.maxBatteryVolt, max_volt)
        self.__update_label(self.gui_app.maxBatteryTemp, max_temp)

    # Updates lights states in the GUI
    def update_lights(self, lights_status: List[bool]) -> None:
        if not self.paused:
            # index is an enumeration, starting at 1
            # lightState is an element in lightStates
            # eval is used to obtain the right label object through its name
            for index, light_status in enumerate(lights_status, 1):
                # Get the light label
                light_label = eval("self.gui_app.l" + str(index))
                # Get the light frame
                light_frame = eval("self.gui_app.lights" + str(index) + "frame")

                if light_status is True:  # Light is on
                    # Set label color to black
                    light_label.setStyleSheet("color: black;")
                    # Set frame color to yellowish
                    light_frame.setStyleSheet("background-color: #d6cc13; border-radius: 15px;")

                else:   # Light is off
                    # Set label color to white
                    light_label.setStyleSheet("color: white;")
                    # Set frame color to yellowish
                    light_frame.setStyleSheet("background-color: black; border-radius: 15px;")

    # Updates switches states in the GUI
    def update_switches(self, switches_status: List[bool]) -> None:
        if not self.paused:
            # index is an enumeration, starting at 1
            # switchState is an element in switchesStates
            # eval is used to obtain the right label object through its name
            for index, switch_status in enumerate(switches_status, 1):
                # Get the switch label
                switch_label = eval("self.gui_app.s" + str(index))
                # Get switch frame
                switch_frame = eval("self.gui_app.switches" + str(index) + "frame")

                if switch_status is True:  # Switch is on
                    # Set label color to black
                    switch_label.setStyleSheet("color: black;")
                    # Set frame color to yellowish
                    switch_frame.setStyleSheet("background-color: #d6cc13; border-radius: 15px;")

                else:  # Switch is off
                    # Set label color to white
                    switch_label.setStyleSheet("color: white;")
                    # Set frame color to yellowish
                    switch_frame.setStyleSheet("background-color: black; border-radius: 15px;")
