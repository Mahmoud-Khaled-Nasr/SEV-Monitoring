from actions.action import Action
from database import database_session


class StopAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # Properly stops reading, closes the port, and stops executing the thread
        self.dispatcher.serial_reader.stop()
        self.dispatcher.current_lap.finish_lap()
        database_session.add(self.dispatcher.current_lap)
        database_session.commit()
