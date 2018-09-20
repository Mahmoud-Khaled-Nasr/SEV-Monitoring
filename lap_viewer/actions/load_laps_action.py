from database.database import Session
from lap_viewer.actions.action import Action
from models.laps.lap import Lap


# Action to load the laps from the database to the GUI
class LoadLapsAction(Action):
    # Constructor
    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self):
        # Open a database session
        session = Session()
        laps = session.query(Lap).all()
        # Add the laps to the GUI
        self.dispatcher.gui_interface.update_laps_list(laps=laps)
        # Close the session
        session.close()
