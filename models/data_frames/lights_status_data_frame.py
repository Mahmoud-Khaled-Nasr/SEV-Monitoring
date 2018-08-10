from typing import List

from sqlalchemy import ForeignKey, Column, Integer, Boolean

from models.data_frames.data_frame import DataFrame, GUIInterface
from definitions import DatabaseTablesNames


class LightsDataFrame(DataFrame):

    __tablename__ = DatabaseTablesNames.LIGHT_TABLE
    __mapper_args__ = {
        'polymorphic_identity': DatabaseTablesNames.LIGHT_TABLE
    }

    id = Column(Integer, ForeignKey(DatabaseTablesNames.DATA_FRAME_TABLE+".id"), primary_key=True)
    head_lights = Column(Boolean, nullable=False)
    tail_lights = Column(Boolean, nullable=False)
    left_indicator = Column(Boolean, nullable=False)
    right_indicator = Column(Boolean, nullable=False)
    high_beam = Column(Boolean, nullable=False)
    brake_light = Column(Boolean, nullable=False)
    backing_light = Column(Boolean, nullable=False)
    daytime_light = Column(Boolean, nullable=False)

    def __init__(self, frame_id: int, frame_value: bytes, headlights: bool, tail_lights: bool,
                 left_indicator: bool, right_indicator: bool, high_beam: bool, brake_light: bool,
                 backing_light: bool, daytime_light: bool):

        super().__init__(frame_id, frame_value)

        self.head_lights: bool = headlights
        self.tail_lights: bool = tail_lights
        self.left_indicator: bool = left_indicator
        self.right_indicator: bool = right_indicator
        self.high_beam: bool = high_beam
        self.brake_light: bool = brake_light
        self.backing_light: bool = backing_light
        self.daytime_light: bool = daytime_light

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Lights Data Frame( frame ID='%d', frame value='%s', headlights='%s', tail lights='%s'" \
               ", left indicator='%s', right indicator='%s', high beam='%s', brake light='%s', " \
               "backing light='%s', daytime light='%s')>" \
               % (self.frame_id, self.frame_value, self.head_lights, self.tail_lights, self.left_indicator,
                  self.right_indicator, self.high_beam, self.brake_light, self.backing_light,
                  self.daytime_light)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        lights_status: List[bool] = [self.head_lights, self.tail_lights, self.left_indicator,
                                     self.right_indicator, self.high_beam, self.brake_light,
                                     self.backing_light, self.daytime_light]
        gui_interface.update_lights(lights_status=lights_status)
