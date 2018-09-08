# TODO check if u can remove this line
import database.database
from dispatcher import Dispatcher
from GUI.GUI_interface import GUIInterface
from input.serial_reader import SerialReader
from input.wifi_reader import WiFiReader

COM_PORT = "COM7"
BAUD_RATE = 9600

broadcase_IP = ' '
broadcase_port = 4211
server_IP = '192.168.4.1'
server_port = 4210

if __name__ == "__main__":

    gui_interface = GUIInterface()
    serial_reader = SerialReader(COM_PORT, BAUD_RATE)
    wifi_reader = WiFiReader(broadcase_IP, broadcase_port, server_IP, server_port)
    dispatcher = Dispatcher(gui_interface=gui_interface, serial_reader=serial_reader, wifi_reader=wifi_reader)
    gui_interface.start_gui()
