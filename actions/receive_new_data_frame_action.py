from queue import Queue

from PyQt5.QtCore import QThread

from actions.action import Action
from database import database_session
from models.data_frames.data_frame import DataFrame


class ReceiveNewDataFrameAction(Action):

    def __init__(self, dispatcher, data_frame):
        super(ReceiveNewDataFrameAction, self).__init__(dispatcher)
        self.data_frame: DataFrame = data_frame

    def execute(self):
        # the session must be used from the dispatcher but there is a problem with autocomplete till fixing it i will
        # use the object directly from the database file
        self.data_frame.lap = self.dispatcher.current_lap
        update_database.add_new_frame(self.data_frame)
        # Update the GUI
        self.data_frame.update_gui(gui_interface=self.dispatcher.gui_interface)
        # updater.start()


class UpdateDatabase (QThread):

    data_frames = Queue()

    def __init__(self):
        super().__init__()

    def add_new_frame(self, frame: DataFrame):
        self.data_frames.put_nowait(frame)

    def run(self):
        while True:
            print("committing")
            frame: DataFrame = self.data_frames.get()
            if frame is None:
                self.quit()
            database_session.add(frame)
            database_session.commit()


update_database = UpdateDatabase()
update_database.start()
