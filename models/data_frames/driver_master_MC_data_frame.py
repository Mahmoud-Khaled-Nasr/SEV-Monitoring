from sqlalchemy import ForeignKey, Column, Integer, Float

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class DriverMasterMCDataFrame(DataFrame):
    __tablename__ = DatabaseTablesNames.DRIVER_MASTER_MC_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.DRIVER_MASTER_MC_TABLE,
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE+".id"), primary_key=True)
    master_motor_current = Column(Float, nullable=False)
    master_motor_speed = Column(Float, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, master_motor_current: float,
                 master_motor_speed: int):
        super().__init__(frame_id, frame_value)
        self.master_motor_current = master_motor_current
        self.master_motor_speed = master_motor_speed

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Driver Master MC Data Frame( frame ID='%d', frame value='%s', " \
               "master motor current='%d', master motor speed='%d')>" % \
               (self.frame_id, self.frame_value, self.master_motor_current, self.master_motor_speed)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_master_motor(master_motor_current=self.master_motor_current,
                                          master_motor_speed=self.master_motor_speed)
