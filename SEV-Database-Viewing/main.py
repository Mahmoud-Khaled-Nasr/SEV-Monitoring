from GUI.GUI_interface import GUIInterface
from dispatcher import Dispatcher


if __name__ == '__main__':
    gui_interface = GUIInterface()
    dispatcher = Dispatcher(gui_interface=gui_interface)
    gui_interface.start_gui()

