import datetime
from abc import ABCMeta, abstractmethod

from sqlalchemy import ForeignKey, Column, Integer, DateTime, VARBINARY
from sqlalchemy.orm import relationship

from database import DatabaseBaseClass
from models.laps.lap import Lap


class DataFrame(DatabaseBaseClass):

    __metaclass__ = ABCMeta
    __tablename__ = 'data_frames'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime, default=datetime.datetime.utcnow())
    frame_id = Column(Integer)
    frame_value = Column(VARBINARY(8))
    lap_id = Column(Integer, ForeignKey(Lap.id))

    lap = relationship("Lap", back_populates=__tablename__)

    @abstractmethod
    def __init__(self, frame_id: int, frame_value: bytes):
        self.frame_id = frame_id
        self.frame_value = frame_value

    @abstractmethod
    def __repr__(self):
        return "<User(record id='%d', time='%s', frame ID='%d', frame value='%s')>" \
               % (self.id, self.time, self.frame_id, self.frame_value)
