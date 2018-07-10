from actions.action import Action
from dispatcher import Dispatcher


class StartAction(Action):

    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)

    def execute(self):
        print("This action is executed when clicking start button")
        # * execute the action
        # * The Action class has an object to a dispatcher the dispatcher has an object of gui this is your class
        # you can use this object to access, edit gui and also i need it to get gui data for example here i need to
        # get the values chosen by user either wifi or usb the GUI package will contain the interface i need to get data

