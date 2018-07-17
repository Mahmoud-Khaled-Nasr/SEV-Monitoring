from actions.action import Action
from database import database_session
from models.data_frames.data_frame import DataFrame
from models.data_frames.currents_data_frame import CurrentsDataFrame


class ReceiveNewDataFrameAction(Action):

    def __init__(self, dispatcher, data_frame):
        super(ReceiveNewDataFrameAction, self).__init__(dispatcher)
        self.data_frame: DataFrame = data_frame

    def execute(self):
        # the session must be used from the dispatcher but there is a problem with autocomplete till fixing it i will
        # use the object directly from the database file
        self.data_frame.lap = self.dispatcher.current_lap
        database_session.add(self.data_frame)
        database_session.commit()
        # Update the GUI
        self.data_frame.update_gui(gui_interface=self.dispatcher.gui_interface)