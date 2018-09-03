import datetime
from abc import ABCMeta, abstractmethod

from sqlalchemy import ForeignKey, Column, Integer, DateTime, VARBINARY, String
from sqlalchemy.orm import relationship

from database.database_base_class import DatabaseBaseClass
from definitions import DatabaseTablesNames
from monitoring.GUI.GUI_interface import GUIInterface


class DataFrame(DatabaseBaseClass):

    # Value used to make DataFrame as an abstract class
    __metaclass__ = ABCMeta
    # The table name needed by SQL Alchemy
    __tablename__ = 'data_frames'

    # Mete data of the table and considered as data members for the DataFrame class
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime, default=datetime.datetime.utcnow())
    frame_id = Column(Integer, nullable=False)
    frame_value = Column(VARBINARY(8), nullable=False)
    lap_id = Column(Integer, ForeignKey("laps.id"), nullable=False)
    type = Column(String(30))

    # Meta Data for sqlalchemy for join inheritance
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.DATA_FRAME_TABLE,
        'polymorphic_on': type
    }

    # link the DataFrame to Lap Class
    lap = relationship("Lap", back_populates=DatabaseTablesNames.DATA_FRAME_TABLE)

    @abstractmethod
    def __init__(self, frame_id: int, frame_value: bytes):
        self.frame_id = frame_id
        self.frame_value = frame_value

    # responsible for the representation of the data when printing the object
    @abstractmethod
    def __repr__(self):
        return "<Data Frame(record id='%d', time='%s', frame ID='%d', frame value='%s', type = '%s')>" \
               % (self.id, self.time, self.frame_id, self.frame_value, self.type)

    # Updates the gui values
    @abstractmethod
    def update_gui(self, gui_interface: GUIInterface) -> None:
        pass
