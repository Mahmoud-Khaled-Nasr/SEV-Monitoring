from actions.action import Action
from dispatcher import Dispatcher


class CreateNewFrameAction(Action):

    def __init__(self, dispatcher: Dispatcher, ):
        super().__init__(dispatcher)

    def execute(self):
        print("This action is executed when new data is received creating frame in db "
              "and call function from gui to update gui")
        # execute the action
