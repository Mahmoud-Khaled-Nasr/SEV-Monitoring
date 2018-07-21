from actions.action import Action
from database import Session
from models.laps.lap import Lap


class StartAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # Start the serial reading thread
        # TODO create gui to enter the name and info of the lap
        self.dispatcher.current_lap = Lap("temp")
        database_session = Session()
        database_session.add(self.dispatcher.current_lap)
        database_session.commit()
        database_session.close()
        self.dispatcher.serial_reader.start()
