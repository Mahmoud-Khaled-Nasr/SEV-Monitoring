from dispatcher import Dispatcher
from actions.create_new_frame_action import CreateNewFrameAction


class Input:

    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher

    def read_new_data(self):
        self.dispatcher.dispatch_new_action(CreateNewFrameAction())
