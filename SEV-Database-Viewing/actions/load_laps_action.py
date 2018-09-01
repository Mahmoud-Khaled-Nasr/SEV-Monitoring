from database.database import Session
from actions.action import Action
from models.laps.lap import Lap


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
        session.close()
