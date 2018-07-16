from actions.action import Action


class StopAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # TODO check this logic because the function in the thread probably runs differently
        # and this will miss things up
        self.dispatcher.serial_interface.terminate_serial_connection()
        self.dispatcher.serial_interface.terminate()
