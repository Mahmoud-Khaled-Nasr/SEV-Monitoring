from struct import unpack

from models.data_frames.data_frame import DataFrame


class LightsDataFrame(DataFrame):
    # A format string to determine how the bytes are parsed
    # > : Big-endian
    # ? : boolean
    _parse_string = ">8?"

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # This function break the data down from bytes to the proper values needed by the class
        # Values are returned in a tuple
        (self.light1, self.light2, self.light3, self.light4, self.light5, self.light6, self.light7,
         self.light8) = unpack(self._parse_string, self.frame_value[0:8])

    # just for showing the data inside the objects in the times of need
    # TODO write the __repr__ return
    def __repr__(self):
        return "<User( frame ID='%d', frame value='%s', battery current='%d', motors current='%d'" \
               ", solar panels current='%d')>" \
               % (self.frame_id, self.frame_value, self.battery_current
                  , self.motors_current, self.solar_panels_current)


