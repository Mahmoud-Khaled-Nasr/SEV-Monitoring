from GUI.GUI_main_window import Ui_MainWindow
from enum import Enum
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.QtGui import QFont, QIcon
from definitions import ConnectionTypes


class ButtonModes(Enum):
    START = 1
    STOP = 2
    PAUSE = 3
    CONTINUE = 4


class GUIActions(QObject):
    # Signals
    signal_start = pyqtSignal(ConnectionTypes)
    signal_stop = pyqtSignal()
    signal_pause = pyqtSignal(bool)

    # Constructor
    def __init__(self, gui_app: Ui_MainWindow):
        super(GUIActions, self).__init__()
        self.gui_app = gui_app
        self.start_stop_button_mode = ButtonModes.START
        self.pause_continue_button_mode = ButtonModes.PAUSE

    # Start/Stop button click action
    def start_stop_button_clicked(self) -> None:
        if self.start_stop_button_mode is ButtonModes.START:  # If the mode is Start
            # Get connection type
            connection_type = self.__get_connection_type()
            # Set the mode and button text to stop
            self.start_stop_button_mode = ButtonModes.STOP
            self.gui_app.start_stop_button.setText("Stop")
            # Emit a start signal
            self.signal_start.emit(connection_type)
        else:  # If the mode is stop
            # Set the mode and button text to start
            self.start_stop_button_mode = ButtonModes.START
            self.gui_app.start_stop_button.setText("Start")
            # Emit a stop signal
            self.signal_stop.emit()

    # Pause/Continue button click action
    def pause_continue_button_clicked(self) -> None:
        if self.pause_continue_button_mode is ButtonModes.PAUSE:  # If the mode is pause
            # Set the mode and button text to continue
            self.pause_continue_button_mode = ButtonModes.CONTINUE
            self.gui_app.pause_continue_button.setText("Continue")
            # Emit a pause signal
            self.signal_pause.emit(True)
        else:  # If the mode is continue
            # Set the mode and button text to pause
            self.pause_continue_button_mode = ButtonModes.PAUSE
            self.gui_app.pause_continue_button.setText("Pause")
            # Emit a continue signal (pause signal with parameter false)
            self.signal_pause.emit(False)

    # Gets the connection type through a message box
    def __get_connection_type(self) -> ConnectionTypes:
        # Create and style the message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Connection Method")
        msg_box.setText("Choose a connection method")
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowIcon(QIcon("GUI/sev-cut.ico"))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        msg_box.setFont(font)
        # Add the buttons
        usb_button = QPushButton("USB")
        wireless_button = QPushButton("WiFi")
        msg_box.addButton(usb_button, QMessageBox.YesRole)
        msg_box.addButton(wireless_button, QMessageBox.NoRole)
        msg_box.exec_()
        if msg_box.clickedButton() is usb_button:
            return ConnectionTypes.USB
        elif msg_box.clickedButton() is wireless_button:
            return ConnectionTypes.WIFI
