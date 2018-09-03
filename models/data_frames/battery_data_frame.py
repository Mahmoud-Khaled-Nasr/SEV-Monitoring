from sqlalchemy import ForeignKey, Column, Integer

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class BatteryDataFrame(DataFrame):

    __tablename__ = DatabaseTablesNames.BATTERY_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.BATTERY_TABLE,
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE + ".id"), primary_key=True)
    battery_volt = Column(Integer, nullable=False)
    battery_temperature = Column(Integer, nullable=False)
    battery_id = Column(Integer, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, voltage: int, temperature: int, battery_id: int):
        super().__init__(frame_id, frame_value)
        self.battery_volt = voltage
        self.battery_temperature = temperature
        self.battery_id = battery_id

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Battery Data Frame( frame ID='%d', frame value='%s',battery id='%d', " \
               "battery volt='%d', battery temperature='%d')>" % \
               (self.frame_id, self.frame_value, self.battery_id, self.battery_volt,
                self.battery_temperature)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_battery(module_number= self.battery_id,
                                     battery_volt=self.battery_volt,
                                     battery_temperature=self.battery_temperature)