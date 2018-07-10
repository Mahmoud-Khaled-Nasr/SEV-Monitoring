from dispatcher import Dispatcher
from actions.start_action import StartAction


class GUI:
    # This is just a dummy class this is your part and i will make it a singleton and get its object via static function

    def __init__(self, dispatcher: Dispatcher):
        self.__dispatcher = dispatcher

    # just an example for button press
    def on_pressing_start_button(self):
        # for example we may adjust the StartAction Class parameters to send for example the type of connection
        self.__dispatcher.dispatch_new_action(StartAction(self.__dispatcher))

    def get_gui_object(self):
        pass
