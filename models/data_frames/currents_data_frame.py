from struct import unpack

from models.data_frames.data_frame import DataFrame, GUIInterface


class CurrentsDataFrame(DataFrame):
    # A format string to determine how the bytes are parsed
    # > : Big-endian
    # H : unsigned short
    _parse_string = ">HHH"

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # This function break the data down from bytes to the proper values needed by the class
        # Values are returned in a tuple
        (self.battery_current, self.motors_current, self.solar_panels_current) \
            = unpack(self._parse_string, self.frame_value[0:6])

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Currents Data Frame( frame ID='%d', frame value='%s', battery current='%d'" \
               ", motors current='%d', solar panels current='%d')>" \
               % (self.frame_id, self.frame_value, self.battery_current
                  , self.motors_current, self.solar_panels_current)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_currents(battery_current=self.battery_current,
                                      motors_current=self.motors_current,
                                      solar_panels_current=self.solar_panels_current)