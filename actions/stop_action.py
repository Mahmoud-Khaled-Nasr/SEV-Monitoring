from actions.action import Action
from dispatcher import Dispatcher


class StopAction(Action):

    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # TODO check this logic because the function in the thread probably runs differently
        # and this will miss things up
        self.dispatcher.serial_interface.terminate()
