from database.database import Session
from lap_viewer.actions.action import Action
from models.laps.lap import Lap


# Action to set the current lap to the selected lap
class ViewLapAction(Action):
    # Constructor
    def __init__(self, dispatcher, lap_id: int):
        self.lap_id = lap_id
        super().__init__(dispatcher)

    def execute(self):
        # Open a session to the database
        session = Session()
        # Query the lap by its id
        laps = session.query(Lap).filter_by(id=self.lap_id).all()  # Should return a list containing one Lap
        if laps:  # Making sure the list returned isn't empty
            lap: Lap = laps[0]
            # Set the current lap
            self.dispatcher.current_lap = lap
        # Close the database session
        session.close()



