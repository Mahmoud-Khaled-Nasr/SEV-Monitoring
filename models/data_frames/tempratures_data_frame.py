from sqlalchemy import ForeignKey, Column, Integer

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class TemperaturesDataFrame(DataFrame):

    __tablename__ = DatabaseTablesNames.TEMPERATURE_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.TEMPERATURE_TABLE,
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE + ".id"), primary_key=True)
    solar_panels_temperature = Column(Integer, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, solar_panels_temperature: int):
        super().__init__(frame_id, frame_value)
        self.solar_panels_temperature = solar_panels_temperature

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Temperatures Data Frame( frame ID='%d', frame value='%s', " \
               "solar panels temperature='%d')>" \
               % (self.frame_id, self.frame_value
                  , self.solar_panels_temperature)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_temperatures(solar_panels_temperature=self.solar_panels_temperature)

