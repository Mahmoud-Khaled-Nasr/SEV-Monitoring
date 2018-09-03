from sqlalchemy import ForeignKey, Column, Integer, Float

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class DriverSlaveMCDataFrame(DataFrame):
    __tablename__ = DatabaseTablesNames.DRIVER_SLAVE_MC_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.DRIVER_SLAVE_MC_TABLE,
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE+".id"), primary_key=True)
    slave_motor_current = Column(Float, nullable=False)
    slave_motor_speed = Column(Float, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, slave_motor_current: float,
                 slave_motor_speed: int):
        super().__init__(frame_id, frame_value)
        self.slave_motor_current = slave_motor_current
        self.slave_motor_speed = slave_motor_speed

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Drive Slave MC Data Frame( frame ID='%d', frame value='%s', slave motor current='%d', " \
               "slave motor speed='%d')>" % \
               (self.frame_id, self.frame_value, self.slave_motor_current, self.slave_motor_speed)

# Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_slave_motor(slave_motor_current=self.slave_motor_current,
                                         slave_motor_speed=self.slave_motor_speed)