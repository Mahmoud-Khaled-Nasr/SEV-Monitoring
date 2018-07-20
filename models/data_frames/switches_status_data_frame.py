from struct import unpack

from models.data_frames.data_frame import DataFrame, GUIInterface


class SwitchesDataFrame(DataFrame):
    NUMBER_OF_SWITCHES = 6

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # Create list of lights
        self.switches_status = []
        # Evaluate the bits as booleans (light status)
        compare_byte = 0b00000001
        for i in range(1, self.NUMBER_OF_SWITCHES + 1):
            self.switches_status[i] = value[0] & compare_byte
            compare_byte = compare_byte << 1

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Switches Data Frames( frame ID='%d', frame value='%s', motor on='%s', forward='%s'" \
               ", reverse='%s', light on='%s', warning='%s', daytime='%s')>" \
               % ((self.frame_id, self.frame_value) + tuple(self.switches_status))

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_switches(switches_status=self.switches_status)