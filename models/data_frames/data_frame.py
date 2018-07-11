from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from abc import ABCMeta, abstractmethod

Base = declarative_base()


class DataFrame(Base):

    __metaclass__ = ABCMeta
    __tablename__ = 'data_frames'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime)
    frame_id = Column(Integer)
    frame_value = Column(String(8))

    @abstractmethod
    def __init__(self, frame_id: int, frame_value: bytes):
        self.frame_id = frame_id
        self.frame_value = frame_value

    '''
    @abstractmethod
    def __repr__(self):
        pass
    '''

    '''
    def __repr__(self):
...        return "<User(name='%s', fullname='%s', password='%s')>" % (
...                             self.name, self.fullname, self.password)
    '''
