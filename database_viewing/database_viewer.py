from database_viewing.GUI.GUI_interface import GUIInterface
from database_viewing.dispatcher import Dispatcher


class DatabaseViewer:

    def __init__(self):
        # Create a gui interface and a dispatcher
        gui_interface = GUIInterface()
        self.dispatcher = Dispatcher(gui_interface=gui_interface)

    def start(self):
        # Start the GUI
        self.dispatcher.gui_interface.start_gui()