from actions.action import Action
from database.database import Session
from database.database import insert_data_frames
from models.laps.lap import Lap


class StartAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # Start the serial reading thread
        # TODO Yosry create gui to enter the name and info of the lap
        self.dispatcher.current_lap = Lap("temp")
        database_session = Session()
        database_session.add(self.dispatcher.current_lap)
        database_session.commit()
        database_session.close()
        # Starting the thread that insert new frames to the database
        insert_data_frames.start()
        # Start the serial reader
        self.dispatcher.serial_reader.start()
