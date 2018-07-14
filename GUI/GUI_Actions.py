from GUI.GUI_MainWindow import Ui_MainWindow
from enum import Enum
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.QtGui import QFont, QIcon


class ButtonModes(Enum):
    START = 1
    STOP = 2
    PAUSE = 3
    CONTINUE = 4


class GUIActions(QObject):
    signal_start = pyqtSignal(int)  # Should add parameter type for connection method 0:usb 1:wireless
    signal_stop = pyqtSignal()
    signal_pause = pyqtSignal(bool)

    def __init__(self, gui_app: Ui_MainWindow):
        super(GUIActions, self).__init__()
        self.gui_app = gui_app
        self.start_stop_button_mode = ButtonModes.START
        self.pause_continue_button_mode = ButtonModes.PAUSE

    def start_stop_button_clicked(self):
        if self.start_stop_button_mode is ButtonModes.START:
            connection_type = self.__get_connection_type()
            self.start_stop_button_mode = ButtonModes.STOP
            self.gui_app.start_stop_button.setText("Stop")
            self.signal_start.emit(connection_type)
        else:
            self.start_stop_button_mode = ButtonModes.START
            self.gui_app.start_stop_button.setText("Start")
            self.signal_stop.emit()

    def pause_continue_button_clicked(self):
        if self.pause_continue_button_mode is ButtonModes.PAUSE:
            self.pause_continue_button_mode = ButtonModes.CONTINUE
            self.gui_app.pause_continue_button.setText("Continue")
            self.signal_pause.emit(True)
        else:
            self.pause_continue_button_mode = ButtonModes.PAUSE
            self.gui_app.pause_continue_button.setText("Pause")
            self.signal_pause.emit(False)

    def __get_connection_type(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Connection Method")
        msg_box.setText("Choose a connection method")
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowIcon(QIcon("GUI/sev-cut.ico"))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(12)
        msg_box.setFont(font)
        msg_box.addButton(QPushButton("USB"), QMessageBox.YesRole)
        msg_box.addButton(QPushButton("Wireless"), QMessageBox.NoRole)
        return msg_box.exec_()
