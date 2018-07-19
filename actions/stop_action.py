from actions.action import Action


class StopAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # Properly stops reading, closes the port, and stops executing the thread
        self.dispatcher.serial_reader.stop()
