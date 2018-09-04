from database_viewing.GUI.GUI_interface import GUIInterface
from database_viewing.dispatcher import Dispatcher


if __name__ == '__main__':
    gui_interface = GUIInterface()
    dispatcher = Dispatcher(gui_interface=gui_interface)
    gui_interface.start_gui()

