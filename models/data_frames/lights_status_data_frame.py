from models.data_frames.data_frame import DataFrame, GUIInterface
from typing import List


class LightsDataFrame(DataFrame):

    def __init__(self, frame_id: int, frame_value: bytes, lights_status: List[bool]):
        super().__init__(frame_id, frame_value)
        self.lights_status = lights_status

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Lights Data Frame( frame ID='%d', frame value='%s', headlights='%s', tail lights='%s'" \
               ", left indicator='%s', right indicator='%s', high beam='%s', brake light='%s', " \
               "backing light='%s', daytime light='%s')>" \
               % ((self.frame_id, self.frame_value) + tuple(self.lights_status))

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_lights(lights_status=self.lights_status)
