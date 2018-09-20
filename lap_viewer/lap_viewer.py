from lap_viewer.GUI.GUI_interface import GUIInterface
from lap_viewer.dispatcher import Dispatcher


class LapViewer:

    def __init__(self):
        # Create a gui interface and a dispatcher
        gui_interface = GUIInterface()
        self.dispatcher = Dispatcher(gui_interface=gui_interface)

    def start(self):
        # Start the GUI
        self.dispatcher.gui_interface.start_gui()