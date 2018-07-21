from models.data_frames.data_frame import DataFrame, GUIInterface
from typing import List


# TODO reimplement this class when the new data frames arrives
class LightsDataFrame(DataFrame):
    NUMBER_OF_LIGHTS = 8

    def __init__(self, frame_id: int, frame_value: bytes):
        super().__init__(frame_id, frame_value)
        # Create list of lights
        self.lights_status: List[bool] = []
        # Evaluate the bits as booleans (light status)
        compare_byte = 0b00000001
        for i in range(1, self.NUMBER_OF_LIGHTS + 1):

            # If the bitwise comparison of the compare byte and the first (and only)
            # byte in "value" isn't equal to a zero, then the bit is 1 (corresponding to true)
            self.lights_status.append(value[0] & compare_byte != 0)
            # Shift the compare byte to compare the next bit
            compare_byte = compare_byte << 1

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Lights Data Frame( frame ID='%d', frame value='%s', headlights='%s', tail lights='%s'" \
               ", left indicator='%s', right indicator='%s', high beam='%s', brake light='%s', " \
               "backing light='%s', daytime light='%s')>" \
               % ((self.frame_id, self.frame_value) + tuple(self.lights_status))

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_lights(lights_status=self.lights_status)
