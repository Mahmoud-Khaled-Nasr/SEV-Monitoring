from sqlalchemy import ForeignKey, Column, Integer

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class BusVoltagesDataFrame(DataFrame):

    __tablename__ = DatabaseTablesNames.BUS_VOLTAGE_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.BUS_VOLTAGE_TABLE
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE + ".id"), primary_key=True)
    DC_bus_voltage = Column(Integer, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, DC_bus_voltage: int):
        super().__init__(frame_id, frame_value)
        self.dc_bus_volt = DC_bus_voltage
        self.x_volt = 0

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Bus Voltage Data Frame( frame ID='%d', frame value='%s', dc bus volt ='%d', x volt ='%d')>" % \
               (self.frame_id, self.frame_value, self.dc_bus_volt, self.x_volt)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_volts(dc_bus_volt=self.dc_bus_volt, xVolt=self.x_volt)