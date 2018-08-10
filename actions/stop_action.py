from actions.action import Action
from database.database import Session
from database.database import insert_data_frames


class StopAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # Properly stops reading, closes the port, and stops executing the thread
        self.dispatcher.serial_reader.stop()
        # Stopping Adding new frames to the database
        insert_data_frames.stop()
        insert_data_frames.wait()
        self.dispatcher.current_lap.finish_lap()
        database_session = Session()
        database_session.add(self.dispatcher.current_lap)
        database_session.commit()
        database_session.close()
