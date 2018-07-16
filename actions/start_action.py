from actions.action import Action


class StartAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        self.dispatcher.serial_reader.start()
