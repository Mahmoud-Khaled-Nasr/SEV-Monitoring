from actions.action import Action


class StartAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # Start the serial reading thread
        self.dispatcher.serial_reader.start()
