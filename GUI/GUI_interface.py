from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from GUI.GUI_main_window import Ui_MainWindow
from GUI.GUI_actions import GUIActions
from typing import List
import sys


class GUIInterface:

    # Constructor
    def __init__(self):
        self.gui_app = Ui_MainWindow()
        # Create a QApplication object
        self.Qapp = QApplication(sys.argv)
        # Create a MainWindow object
        self.main_window = QMainWindow()
        # Setup the user interface
        self.gui_app.setupUi(self.main_window)
        # Maximize the main window
        self.main_window.showMaximized()
        # Create a GUI Actions object
        self.gui_actions = GUIActions(self.gui_app)
        # Set paused flag as false
        self.paused = False
        # Connect buttons to actions
        self.__set_button_connections()

    def start_gui(self) -> None:
        # Start the main event loop
        sys.exit(self.Qapp.exec_())

    # Private method for connecting the buttons clicks to their action
    def __set_button_connections(self) -> None:
        self.gui_app.start_stop_button.clicked.connect(self.gui_actions.start_stop_button_clicked)
        self.gui_app.pause_continue_button.clicked.connect(self.gui_actions.pause_continue_button_clicked)
        self.gui_actions.signal_pause.connect(self.set_paused)

    # Sets the paused flag (slot for the pause signal)
    def set_paused(self, is_paused: bool) -> None:
        self.paused = is_paused

    # Updates the currents on the GUI
    def update_currents(self, battery_current: float, motors_current: float, solar_panels_current: float):
        if not self.paused:
            # Convert the passed floats to strings with precision 2 dp
            #  then set it as text for the output label
            self.gui_app.batteryCurrent.setText("{:.2f}".format(battery_current))
            self.gui_app.motorsCurrent.setText("{:.2f}".format(motors_current))
            self.gui_app.spanelsCurrent.setText("{:.2f}".format(solar_panels_current))

    # Updates the voltages on the GUI
    def update_volts(self, dc_bus_volt: float, xVolt: float):
        if not self.paused:
            # Convert the passed floats to strings with precision 2 dp
            # then set it as text for the output label
            self.gui_app.dcBusVolt.setText("{:.2f}".format(dc_bus_volt))
            self.gui_app.xVolt.setText("{:.2f}".format(xVolt))

    # Updates the temperatures on the GUI
    def update_temperatures(self, xTemp: float, solar_panels_temperature: float, yTemp: float):
        if not self.paused:
            # Convert the passed floats to strings with precision 2 dp
            # then set it as text for the output label
            self.gui_app.xTemp.setText("{:.2f}".format(xTemp))
            self.gui_app.spanelsTemp.setText("{:.2f}".format(solar_panels_temperature))
            self.gui_app.yTemp.setText("{:.2f}".format(yTemp))

    # Updates the Master Motor MC Data on the GUI
    def update_master_mc(self, master_current: float, master_speed: float):
        if not self.paused:
            # Convert the passed floats to strings with precision 2 dp
            # then set it as text for the output label
            self.gui_app.masterCurrent.setText("{:.2f}".format(master_current))
            self.gui_app.masterSpeed.setText("{:.2f}".format(master_speed))

    # Updates the Slave Motor MC Data on the GUI
    def update_slave_mc(self, slave_current: float, slave_speed: float):
        if not self.paused:
            # Convert the passed floats to strings with precision 2 dp
            # then set it as text for the output label
            self.gui_app.slaveCurrent.setText("{:.2f}".format(slave_current))
            self.gui_app.slaveSpeed.setText("{:.2f}".format(slave_speed))

    # Updates the batteries data on the GUI
    def update_batteries_data(self, batteries_volts: List[float], batteries_temps: List[float]):
        if not self.paused:
            # index is an enumeration, starting at 1
            # volt and temp are elements in batteryVolts and batteryTemps respectively
            # eval is used to obtain the right label object through its name
            for index, (volt, temp) in enumerate(zip(batteries_volts, batteries_temps), 1):
                # Get volt label
                volt_label = eval("self.gui_app.batteryVolt" + str(index))
                # Get temperature label
                temp_label = eval("self.gui_app.batteryTemp" + str(index))

                # Convert the floats into strings with precision of 2 dp
                # then set it as text for the output labels
                volt_label.setText("{:.2f}".format(volt))
                temp_label.setText("{:.2f}".format(temp))

            # Set the highlights

            max_volt = max(batteries_volts)
            min_volt = min(batteries_volts)
            max_temp = max(batteries_temps)

            # Convert the floats into strings with precision of 2 dp
            # then set it as text for the output labels
            self.gui_app.maxBatteryVolt.setText("{:.2f}".format(max_volt))
            self.gui_app.minBatteryVolt.setText("{:.2f}".format(min_volt))
            self.gui_app.maxBatteryTemp.setText("{:.2f}".format(max_temp))

    # Updates lights states in the GUI
    def update_lights(self, lights_status: List[bool]):
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

