import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import DatabaseBaseClass


class Lap(DatabaseBaseClass):

    __tablename__ = 'laps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(DateTime, default=datetime.datetime.utcnow())
    finish_time = Column(DateTime, nullable=True)
    name = Column(String)
    comments = Column(String, nullable=True)

    data_frames = relationship("DataFrame")

    def __init__(self, name: str, comments: str = None):
        self.name = name
        if comments is None:
            self.comments = ""
        else:
            self.comments = comments

    def __repr__(self):
        return "<Lap(lap id='%d', starting time='%s', finishing time='%s', name='%s', comments='%s')>" \
               % (self.id, self.start_time, self.finish_time, self.name, self.comments)