from sqlalchemy import ForeignKey, Column, Integer

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class CurrentsDataFrame(DataFrame):

    __tablename__ = DatabaseTablesNames.CURRENT_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.CURRENT_TABLE,
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE+".id"), primary_key=True)
    battery_current = Column(Integer, nullable=False)
    motors_current = Column(Integer, nullable=False)
    solar_panels_current = Column(Integer, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, battery_current: int, motors_current: int, solar_panels_current: int):
        super().__init__(frame_id, frame_value)
        self.battery_current = battery_current
        self.motors_current = motors_current
        self.solar_panels_current = solar_panels_current

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Currents Data Frame( frame ID='%d', frame value='%s', battery current='%d'" \
               ", motors current='%d', solar panels current='%d')>" \
               % (self.frame_id, self.frame_value, self.battery_current,
                  self.motors_current, self.solar_panels_current)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_currents(battery_current=self.battery_current,
                                      motors_current=self.motors_current,
                                      solar_panels_current=self.solar_panels_current)