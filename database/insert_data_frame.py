from queue import Queue

from PyQt5.QtCore import QThread

from database.database import Session
from models.data_frames.data_frame import DataFrame


class InsertDataFrames (QThread):

    data_frames = Queue()

    def __init__(self):
        super().__init__()
        self.database_session = Session()
        self.operate: bool = True

    def add_new_frame(self, frame: DataFrame):
        self.data_frames.put_nowait(frame)

    def run(self):
        self.operate = True
        time_out = 7
        while self.operate:
            print("committing")
            frame: DataFrame = self.data_frames.get(timeout=time_out)
            if frame is None:
                continue
            self.database_session.add(frame)
            self.database_session.commit()

        # when the serial stops all the data in the queue should be flushed and the session is closed
        while self.data_frames.qsize() != 0:
            frame: DataFrame = self.data_frames.get_nowait()
            self.database_session.add(frame)

        self.database_session.commit()
        self.database_session.close()

    def stop(self):
        self.operate = False
