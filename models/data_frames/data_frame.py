import datetime
from abc import ABCMeta, abstractmethod

from sqlalchemy import Column, Integer, String, DateTime

from globals import DatabaseBaseClass


class DataFrame(DatabaseBaseClass):

    __metaclass__ = ABCMeta
    __tablename__ = 'data_frames'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime, default=datetime.datetime.utcnow())
    frame_id = Column(Integer)
    frame_value = Column(String(8))

    @abstractmethod
    def __init__(self, frame_id: int, frame_value: bytes):
        self.frame_id = frame_id
        self.frame_value = frame_value

    @abstractmethod
    def __repr__(self):
        return "<User(record id='%d', time='%s', frame ID='%d', frame value='%s')>" \
               % (self.id, self.time, self.frame_id, self.frame_value)


