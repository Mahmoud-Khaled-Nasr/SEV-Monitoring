from database import database_session
from dispatcher import Dispatcher
from GUI.GUI_interface import GUIInterface
from input.serial_reader import SerialReader

COM_PORT = "COM7"
BAUD_RATE = 9600

if __name__ == "__main__":

    gui_interface = GUIInterface()
    serial_interface = SerialReader(COM_PORT, BAUD_RATE)
    dispatcher = Dispatcher(gui_interface=gui_interface, serial_interface=serial_interface,
                            database_session=database_session)
    # serial_interface.start()
    gui_interface.start_gui()

