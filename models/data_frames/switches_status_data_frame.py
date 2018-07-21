from typing import List

from models.data_frames.data_frame import DataFrame, GUIInterface

# TODO reimplement this class when the new data frames arrives
class SwitchesDataFrame(DataFrame):
    NUMBER_OF_SWITCHES = 6

    def __init__(self, frame_id: int, frame_value: bytes):
        super().__init__(frame_id, frame_value)
        # Create list of switches
        self.switches_status: List[bool] = []
        # Evaluate the bits as booleans (switch status)
        compare_byte = 0b00000001
        for i in range(1, self.NUMBER_OF_SWITCHES + 1):
            # If the bitwise comparison of the compare byte and the first (and only)
            # byte in "value" isn't equal to a zero, then the bit is 1 (corresponding to true)
            self.switches_status.append(value[0] & compare_byte != 0)
            # Shift the compare byte to compare the next bit
            compare_byte = compare_byte << 1
    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Switches Data Frames( frame ID='%d', frame value='%s', motor on='%s', forward='%s'" \
               ", reverse='%s', light on='%s', warning='%s', daytime='%s')>" \
               % ((self.frame_id, self.frame_value) + tuple(self.switches_status))

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_switches(switches_status=self.switches_status)