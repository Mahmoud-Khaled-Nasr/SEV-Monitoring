from typing import List

from sqlalchemy import ForeignKey, Column, Integer, Boolean

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class SwitchesDataFrame(DataFrame):

    __tablename__ = DatabaseTablesNames.SWITCH_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.SWITCH_TABLE
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE + ".id"), primary_key=True)
    motor_on = Column(Boolean, nullable=False)
    forward = Column(Boolean, nullable=False)
    reverse = Column(Boolean, nullable=False)
    light_on = Column(Boolean, nullable=False)
    warning = Column(Boolean, nullable=False)
    daytime = Column(Boolean, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, motor_on: bool, forward: bool,
                 reverse: bool, light_on: bool, warning: bool, daytime: bool):

        super().__init__(frame_id, frame_value)

        self.motor_on: bool = motor_on
        self.forward: bool = forward
        self.reverse: bool = reverse
        self.light_on: bool = light_on
        self.warning: bool = warning
        self.daytime: bool = daytime

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Switches Data Frames( frame ID='%d', frame value='%s', motor on='%s', forward='%s'" \
               ", reverse='%s', light on='%s', warning='%s', daytime='%s')>" \
               % (self.frame_id, self.frame_value, self.motor_on, self.forward, self.reverse,
                  self.light_on, self.warning, self.daytime)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        switches_status: List[bool] = [self.motor_on, self.forward, self.reverse,
                                       self.light_on, self.warning, self.daytime]
        gui_interface.update_switches(switches_status=switches_status)
