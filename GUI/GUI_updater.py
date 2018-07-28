from definitions import Ranges, Tolerances
from PyQt5.QtWidgets import QLabel
from GUI.GUI_main_window import Ui_MainWindow
from typing import List


class GUIUpdater:
    def __init__(self, gui_app: Ui_MainWindow):
        self.gui_app = gui_app
        # Set paused flag as false
        self.paused = False
        # Create needed dictionaries
        self.ranges = {}
        self.tolerances = {}
        self.current_values = {}
        self.batteries_volts = {}
        self.batteries_temperatures = {}
        # Initialize the dictionaries
        self.__init_ranges_dict()
        self.__init_tolerances_dict()

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
        self.ranges[self.gui_app.xVolt] = Ranges.charge_rate
        self.ranges[self.gui_app.dcBusVolt] = Ranges.dc_bus_volt
        # Master Motor
        self.ranges[self.gui_app.masterCurrent] = Ranges.driver_master_motor_current
        self.ranges[self.gui_app.masterSpeed] = Ranges.driver_master_motor_speed
        # Slave Motor
        self.ranges[self.gui_app.slaveCurrent] = Ranges.driver_slave_motor_current
        self.ranges[self.gui_app.slaveSpeed] = Ranges.driver_slave_motor_speed
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
        self.tolerances[self.gui_app.xVolt] = Tolerances.charge_rate
        self.tolerances[self.gui_app.dcBusVolt] = Tolerances.dc_bus_volt
        # Master Motor
        self.tolerances[self.gui_app.masterCurrent] = Tolerances.driver_master_motor_current
        self.tolerances[self.gui_app.masterSpeed] = Tolerances.driver_master_motor_speed
        # Slave Motor
        self.tolerances[self.gui_app.slaveCurrent] = Tolerances.driver_slave_motor_current
        self.tolerances[self.gui_app.slaveSpeed] = Tolerances.driver_slave_motor_speed
        # Battery Modules
        for i in range(1, 15):
            self.tolerances[eval("self.gui_app.batteryVolt" + str(i))] = Tolerances.battery_module_volt
            self.tolerances[eval("self.gui_app.batteryTemp" + str(i))] = Tolerances.battery_module_temperature

    # Private method: Checks if a value is in range for a certain type of data
    def __is_in_range(self, data_label: QLabel, value: float) -> bool:
        (minimum, maximum) = self.ranges[data_label]
        if minimum <= value <= maximum:
            return True
        else:
            return False

    # Private method: Checks if the change in value is tolerable
    def __is_tolerable(self, data_label: QLabel, value: float) -> bool:
        # No existing value yet, not tolerable
        if data_label not in self.current_values:
            return False
        # The difference magnitude is below the tolerance
        elif abs(value - self.current_values[data_label]) < self.tolerances[data_label]:
            return True
        else:
            return False

    # Updates the label with the value
    def update_label(self, data_label: QLabel, value: float) -> None:
        if not self.paused:
            # Check if the change in value is not tolerable
            if not self.__is_tolerable(data_label, value):
                # Update the current value
                self.current_values[data_label] = value
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

    # Updates switches status
    def update_switches(self, switches_status: List[bool]):
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

    # Updates lights status
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

                else:  # Light is off
                    # Set label color to white
                    light_label.setStyleSheet("color: white;")
                    # Set frame color to yellowish
                    light_frame.setStyleSheet("background-color: black; border-radius: 15px;")

    # Updates the batteries data
    def update_battery(self, module_number: int, battery_volt: float, battery_temp: float) -> None:
        if not self.paused:
            # Get volt label
            volt_label = eval("self.gui_app.batteryVolt" + str(module_number))
            # Get temperature label
            temp_label = eval("self.gui_app.batteryTemp" + str(module_number))

            # Update Battery Volt
            # Check if the change in value is not tolerable
            if not self.__is_tolerable(volt_label, battery_volt):
                # Update the current value
                self.current_values[volt_label] = battery_volt
                self.batteries_volts[volt_label] = battery_volt
                # Convert the passed floats to strings with precision 2 dp
                # then set it as text for the output label
                volt_label.setText("{:.2f}".format(battery_volt))
                # Default stylesheets for labels and their frames
                stylesheet = "color: black;"
                parent_frame = volt_label.parent().objectName()
                frame_stylesheet = "QFrame#" + parent_frame + "{border: 1px solid #828790;}"
                # Check if it is out of range
                if not self.__is_in_range(volt_label, battery_volt):
                    #  Out-of-range stylesheets
                    stylesheet = "color: #dd0000;"
                    frame_stylesheet = "QFrame#" + parent_frame + "{border: 1px solid #dd0000;}"
                # Set stylesheets
                volt_label.setStyleSheet(stylesheet)
                volt_label.parent().setStyleSheet(frame_stylesheet)

            # Update Battery Temperature
            # Check if the change in value is not tolerable
            if not self.__is_tolerable(temp_label, battery_temp):
                # Update the current value
                self.current_values[temp_label] = battery_temp
                self.batteries_volts[temp_label] = battery_temp
                # Convert the passed floats to strings with precision 2 dp
                # then set it as text for the output label
                temp_label.setText("{:.2f}".format(battery_temp))
                # Default stylesheets for labels and their frames
                stylesheet = "color: black;"
                parent_frame = temp_label.parent().objectName()
                frame_stylesheet = "QFrame#" + parent_frame + "{border: 1px solid #828790;}"
                # Check if it is out of range
                if not self.__is_in_range(temp_label, battery_temp):
                    #  Out-of-range stylesheets
                    stylesheet = "color: #dd0000;"
                    frame_stylesheet = "QFrame#" + parent_frame + "{border: 1px solid #dd0000;}"
                # Set stylesheets
                temp_label.setStyleSheet(stylesheet)
                temp_label.parent().setStyleSheet(frame_stylesheet)

            # Set the highlights
            if not self.batteries_volts:  # If the dictionary is empty; initial frame
                max_volt = battery_volt
                min_volt = battery_volt
            else:
                max_volt = max(list(self.batteries_volts.values()))
                min_volt = min(list(self.batteries_volts.values()))

            if not self.batteries_temperatures:  # If the dictionary is empty; initial frame
                max_temp = battery_temp
            else:
                max_temp = max(list(self.batteries_temperatures.values()))

            # Updates the labels with the given values
            self.update_label(self.gui_app.minBatteryVolt, min_volt)
            self.update_label(self.gui_app.maxBatteryVolt, max_volt)
            self.update_label(self.gui_app.maxBatteryTemp, max_temp)

    # Sets the paused flag (slot for the pause signal)
    def set_paused(self, is_paused: bool) -> None:
        self.paused = is_paused