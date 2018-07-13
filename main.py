from database import database_session
from dispatcher import Dispatcher
from GUI.GUI_Interface import GUIApp
from input.input import SerialInterface

COM_PORT = "COM7"
BAUD_RATE = 9600

if __name__ == "__main__":

    app = GUIApp()
    serial_interface = SerialInterface(COM_PORT, BAUD_RATE)
    dispatcher = Dispatcher(gui_interface=app, serial_interface=serial_interface,
                            database_session=database_session)
    # serial_interface.start()
    app.start_gui()
