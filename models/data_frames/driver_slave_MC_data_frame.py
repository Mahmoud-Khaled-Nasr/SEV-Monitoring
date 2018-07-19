from struct import unpack

from models.data_frames.data_frame import DataFrame, GUIInterface


class DriverSlaveMCDataFrame(DataFrame):
    # A format string to determine how the bytes are parsed
    # > : Big-endian
    # H : unsigned short
    _parse_string = ">HH"

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # This function break the data down from bytes to the proper values needed by the class
        # Values are returned in a tuple
        (self.slave_motor_current, self.slave_motor_speed) \
            = unpack(self._parse_string, self.frame_value[0:4])

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<User( frame ID='%d', frame value='%s', slave motor current='%d', slave motor speed='%d')>" % \
               (self.frame_id, self.frame_value, self.slave_motor_current, self.slave_motor_speed)

# Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_slave_mc(slave_current=self.slave_motor_current,
                                      slave_speed=self.slave_motor_speed)