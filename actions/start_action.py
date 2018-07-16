from actions.action import Action
from dispatcher import Dispatcher


class StartAction(Action):

    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        self.dispatcher.serial_interface.start()
