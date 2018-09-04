from database.database import Session
from database_viewing.actions.action import Action
from models.laps.lap import Lap


class ViewLapAction(Action):
    # Constructor
    def __init__(self, dispatcher, lap_id: int):
        super().__init__(dispatcher)
        session = Session()
        self.lap: Lap = session.query(Lap).filter_by(id = lap_id).all()[0]  # Should return a list containing one Lap
        session.close()
        # print(self.lap)

    def execute(self):
        self.dispatcher.current_lap = self.lap

