from struct import unpack

from models.data_frames.data_frame import DataFrame, GUIInterface


# TODO reimplement this class when the new data frames arrives
class DriverMasterMCDataFrame(DataFrame):
    # A format string to determine how the bytes are parsed
    # > : Big-endian
    # H : unsigned short
    _parse_string = ">HH"

    def __init__(self, frame_id: int, frame_value: bytes):
        super().__init__(frame_id, frame_value)
        # This function break the data down from bytes to the proper values needed by the class
        # Values are returned in a tuple
        (self.master_motor_current, self.master_motor_speed) \
            = unpack(self._parse_string, self.frame_value[0:4])

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Driver Master MC Data Frame( frame ID='%d', frame value='%s', " \
               "master motor current='%d', master motor speed='%d')>" % \
               (self.frame_id, self.frame_value, self.master_motor_current, self.master_motor_speed)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_master_motor(master_motor_current=self.master_motor_current,
                                          master_motor_speed=self.master_motor_speed)
