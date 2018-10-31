from database.database import Session
from lap_viewer.actions.action import Action
from models.laps.lap import Lap


# Action for deleting a lap from the database
class DeleteLapAction(Action):
    # Constructor
    def __init__(self, dispatcher, lap_id: int):
        super().__init__(dispatcher)
        self.lap_id = lap_id

    def execute(self):
        # Open a session to the database
        session: Session = Session()
        # Delete the lap from the laps table
        lap = session.query(Lap).filter(Lap.id == self.lap_id).first()
        session.delete(lap)
        # Commit changes to the database and close the session
        session.commit()
        session.close()
