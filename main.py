from GUI.GUI import GUI
from dispatcher import Dispatcher

if __name__ == "__main__":
    dispatcher = Dispatcher()
    gui = GUI(dispatcher)
    dispatcher.set_gui_object(gui)
