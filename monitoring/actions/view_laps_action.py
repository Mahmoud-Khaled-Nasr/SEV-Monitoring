from monitoring.actions.action import Action
from subprocess import Popen


class ViewLapsAction(Action):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    def execute(self) -> None:
        # Start the database viewer in a new process
        Popen(['python', '../database_viewing/monitoring.py'])