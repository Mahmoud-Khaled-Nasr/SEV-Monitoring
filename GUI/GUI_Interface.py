from PyQt5 import QtWidgets
from GUI.GUI_Qt import Ui_MainWindow
from typing import List
import sys


class GUIApp(Ui_MainWindow):

    # Constructor
    def __init__(self):
        # Create a QApplication object
        self.Qapp = QtWidgets.QApplication(sys.argv)
        # Create a MainWindow object
        self.MainWindow = QtWidgets.QMainWindow()
        # Setup the user interface
        self.setupUi(self.MainWindow)
        # Maximize the main window
        self.MainWindow.showMaximized()

    def start_gui(self):
        # Start the main event loop
        sys.exit(self.Qapp.exec_())

    # Updates the currents on the GUI
    def updateCurrents(self, batteryCurrent: float, motorsCurrent: float, solarPanelsCurrent: float):
        # Convert the passed floats to strings with precision 2 dp
        #  then set it as text for the output label
        self.batteryCurrent.setText("{:.2f}".format(batteryCurrent))
        self.motorsCurrent.setText("{:.2f}".format(motorsCurrent))
        self.spanelsCurrent.setText("{:.2f}".format(solarPanelsCurrent))


    # Updates the voltages on the GUI
    def updateVolts(self, DCBusVolt: float, xVolt: float):
        # Convert the passed floats to strings with precision 2 dp
        # then set it as text for the output label
        self.dcBusVolt.setText("{:.2f}".format(DCBusVolt))
        self.xVolt.setText("{:.2f}".format(xVolt))


    # Updates the temperatures on the GUI
    def updateTemps(self, xTemp: float, solarPanelsTemp: float, yTemp: float):
        # Convert the passed floats to strings with precision 2 dp
        # then set it as text for the output label
        self.xTemp.setText("{:.2f}".format(xTemp))
        self.spanelsTemp.setText("{:.2f}".format(solarPanelsTemp))
        self.yTemp.setText("{:.2f}".format(yTemp))


    # Updates the Master Motor MC Data on the GUI
    def updateMasterMC(self, masterCurrent: float, masterSpeed: float):
        # Convert the passed floats to strings with precision 2 dp
        # then set it as text for the output label
        self.masterCurrent.setText("{:.2f}".format(masterCurrent))
        self.masterSpeed.setText("{:.2f}".format(masterSpeed))


    # Updates the Slave Motor MC Data on the GUI
    def updateSlaveMC(self, slaveCurrent: float, slaveSpeed: float):
        # Convert the passed floats to strings with precision 2 dp
        # then set it as text for the output label
        self.slaveCurrent.setText("{:.2f}".format(slaveCurrent))
        self.slaveSpeed.setText("{:.2f}".format(slaveSpeed))


    # Updates the batteries data on the GUI
    def updateBatteriesData(self, batteryVolts: List[float], batteryTemps: List[float]):
        # index is an enumeration, starting at 1
        # volt and temp are elements in batteryVolts and batteryTemps respectively
        # eval is used to obtain the right label object through its name
        for index, (volt, temp) in enumerate(zip(batteryVolts, batteryTemps), 1):
            # Get volt label
            voltLabel = eval("self.batteryVolt" + str(index))
            # Get temperature label
            tempLabel = eval("self.batteryTemp" + str(index))

            # Convert the floats into strings with precision of 2 dp
            # then set it as text for the output labels
            voltLabel.setText("{:.2f}".format(volt))
            tempLabel.setText("{:.2f}".format(temp))

        # Set the highlights

        maxVolt = max(batteryVolts)
        minVolt = min(batteryVolts)
        maxTemp = max(batteryTemps)

        # Convert the floats into strings with precision of 2 dp
        # then set it as text for the output labels
        self.maxBatteryVolt.setText("{:.2f}".format(maxVolt))
        self.minBatteryVolt.setText("{:.2f}".format(minVolt))
        self.maxBatteryTemp.setText("{:.2f}".format(maxTemp))


    # Updates lights states in the GUI
    def updateLights(self, lightsStates: List[bool]):
        # index is an enumeration, starting at 1
        # lightState is an element in lightStates
        # eval is used to obtain the right label object through its name
        for index, lightState in enumerate(lightsStates, 1):
            # Get the light label
            lightLabel = eval("self.l" + str(index))
            # Get frame label
            lightFrame = eval("self.lights" + str(index) + "frame")

            if(lightState is True): # Light is on
                # Set label color to black
                lightLabel.setStyleSheet("color: black;")
                # Set frame color to yellowish
                lightFrame.setStyleSheet("background-color: #d6cc13;\n"
                    "border-radius: 15px;\n"
                    "")

            else:   # Light is off
                # Set label color to white
                lightLabel.setStyleSheet("color: white;")
                # Set frame color to yellowish
                lightFrame.setStyleSheet("background-color: black;\n"
                    "border-radius: 15px;\n"
                    "")



    # Updates switches states in the GUI
    def updateSwitches(self, switchesStates: List[bool]):
        # index is an enumeration, starting at 1
        # switchState is an element in switchesStates
        # eval is used to obtain the right label object through its name
        for index, switchState in enumerate(switchesStates, 1):
            # Get the light label
            switchLabel = eval("self.s" + str(index))
            # Get frame label
            switchFrame = eval("self.switches" + str(index) + "frame")

            if (lightState is True):  # Light is on
                # Set label color to black
                switchLabel.setStyleSheet("color: black;")
                # Set frame color to yellowish
                switchFrame.setStyleSheet("background-color: #d6cc13;\n"
                                         "border-radius: 15px;\n"
                                         "")

            else:  # Light is off
                # Set label color to white
                switchLabel.setStyleSheet("color: white;")
                # Set frame color to yellowish
                switchFrame.setStyleSheet("background-color: black;\n"
                                         "border-radius: 15px;\n"
                                         "")
