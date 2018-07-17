from struct import unpack

from models.data_frames.data_frame import DataFrame, GUIInterface


class BatteryDataFrame(DataFrame):
    # A format string to determine how the bytes are parsed
    # > : Big-endian
    # H : unsigned short
    # h : signed short
    _parse_string = ">Hh"

    def __init__(self, frame_id: int, value: bytes, module_number: int):
        # TODO add module number
        super().__init__(frame_id, value)
        # This function break the data down from bytes to the proper values needed by the class
        # Values are returned in a tuple
        (self.battery_volt, self.battery_temperature) \
            = unpack(self._parse_string, self.frame_value[0:4])
        # Set the module number
        self.module_number = module_number

    # just for showing the data inside the objects in the times of need
    # TODO add module number
    def __repr__(self):
        return "<User( frame ID='%d', frame value='%s', module volt='%d', module temperature='%d')>" % \
               (self.frame_id, self.frame_value, self.battery_volt, self.battery_temperature)

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_battery(module_number= self.module_number,
                                     battery_volt=self.battery_volt,
                                     battery_temperature=self.battery_temperature)