from struct import unpack

from models.data_frames.data_frame import DataFrame, GUIInterface


class TemperaturesDataFrame(DataFrame):
    # A format string to determine how the bytes are parsed
    # > : Big-endian
    # h : signed short
    _parse_string = ">hhh"

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # This function break the data down from bytes to the proper values needed by the class
        # Values are returned in a tuple
        (self.x_temperature, self.solar_panels_temperature, self.y_temperature) \
            = unpack(self._parse_string, self.frame_value[0:6])

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Temperatures Data Frame( frame ID='%d', frame value='%s', x temperature='%d', " \
               "solar panels temperature='%d', y temperature='%d')>" \
               % (self.frame_id, self.frame_value, self.x_temperature
                  , self.solar_panels_temperature, self.y_temperature)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_temperatures(xTemp=self.x_temperature,
                                          solar_panels_temperature=self.solar_panels_temperature,
                                          yTemp=self.y_temperature)

