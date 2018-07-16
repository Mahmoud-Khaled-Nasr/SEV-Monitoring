from struct import unpack

from models.data_frames.data_frame import DataFrame


class CurrentDataFrame(DataFrame):

    _parse_string = ">hhh"

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # This function break the data down from bytes to the proper values needed by the class
        self.battery_current, self.motors_current, self.solar_panels_current \
            = unpack(self._parse_string, self.frame_value[0:6])

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<User( frame ID='%d', frame value='%s', battery current='%d', motors current='%d'" \
               ", solar panels current='%d')>" \
               % (self.frame_id, self.frame_value, self.battery_current
                  , self.motors_current, self.solar_panels_current)

