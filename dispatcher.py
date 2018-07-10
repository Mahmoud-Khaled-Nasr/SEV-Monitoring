from actions.action import Action


class Dispatcher:

    __active_frames_list = []
    __active_lap = None
    gui = None

    def __init__(self):
        pass

    def dispatch_new_action(self, action: Action):
        action.execute()

    def set_gui_object(self, gui):
        self.gui = gui
