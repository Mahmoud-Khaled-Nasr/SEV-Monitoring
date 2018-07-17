from struct import unpack

from models.data_frames.data_frame import DataFrame, GUIInterface


class BusVoltagesDataFrame(DataFrame):
    # A format string to determine how the bytes are parsed
    # > : Big-endian
    # H : unsigned short
    _parse_string = ">HH"

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # This function break the data down from bytes to the proper values needed by the class
        # Values are returned in a tuple
        (self.dc_bus_volt, self.x_volt) \
            = unpack(self._parse_string, self.frame_value[0:4])

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<User( frame ID='%d', frame value='%s', dc bus volt ='%d', x volt ='%d')>" % \
               (self.frame_id, self.frame_value, self.dc_bus_volt, self.x_volt)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_volts(dc_bus_volt=self.dc_bus_volt, xVolt=self.x_volt)