from queue import Queue, Empty

from PyQt5.QtCore import QThread

from database.database import Session
from models.data_frames.data_frame import DataFrame


class InsertDataFrames (QThread):

    def __init__(self):
        super().__init__()
        self.database_session = Session()
        self.data_frames_queue = Queue()
        self.operate: bool = True

    def add_new_frame(self, frame: DataFrame):
        self.data_frames_queue.put_nowait(frame)

    def run(self):
        self.operate = True
        time_out = 1
        while self.operate:
            print("committing")
            try:
                frame: DataFrame = self.data_frames_queue.get(timeout=time_out)
            # If the queue is empty, skip adding to the database
            except Empty:
                continue
            self.database_session.add(frame)
            self.database_session.commit()

        # when the serial stops all the data in the queue should be flushed and the session is closed
        while self.data_frames_queue.qsize() != 0:
            frame: DataFrame = self.data_frames_queue.get_nowait()
            self.database_session.add(frame)

        self.database_session.commit()
        self.database_session.close()

    def stop(self):
        self.operate = False
