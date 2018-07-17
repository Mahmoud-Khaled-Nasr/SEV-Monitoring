import datetime
from abc import ABCMeta, abstractmethod

from sqlalchemy import ForeignKey, Column, Integer, DateTime, VARBINARY
from sqlalchemy.orm import relationship

from database import DatabaseBaseClass

from GUI.GUI_interface import GUIInterface
# from models.laps.lap import Lap


class DataFrame(DatabaseBaseClass):

    # Value used to make DataFrame as an abstract class
    __metaclass__ = ABCMeta
    # The table name needed by SQL Alchemy
    __tablename__ = 'data_frames'

    # Mete data of the table and considered as data members for the DataFrame class
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime, default=datetime.datetime.utcnow())
    frame_id = Column(Integer)
    frame_value = Column(VARBINARY(8))
    lap_id = Column(Integer, ForeignKey("laps.id"), nullable=False)

    # link the DataFrame to Lap Class
    lap = relationship("Lap", back_populates="data_frames")

    @abstractmethod
    def __init__(self, frame_id: int, frame_value: bytes):
        self.frame_id = frame_id
        self.frame_value = frame_value

    # responsible for the representation of the data when printing the object
    @abstractmethod
    def __repr__(self):
        return "<User(record id='%d', time='%s', frame ID='%d', frame value='%s')>" \
               % (self.id, self.time, self.frame_id, self.frame_value)

    # Updates the gui values
    @abstractmethod
    def update_gui(self, gui_interface: GUIInterface) -> None:
        pass