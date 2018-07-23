from typing import List

from models.data_frames.data_frame import DataFrame, GUIInterface


# TODO reimplement this class when the new data frames arrives
class SwitchesDataFrame(DataFrame):

    def __init__(self, frame_id: int, frame_value: bytes, switches_status: List[bool]):
        super().__init__(frame_id, frame_value)
        self.switches_status = switches_status

    # just for showing the data inside the objects in the times of need
    def __repr__(self):
        return "<Switches Data Frames( frame ID='%d', frame value='%s', motor on='%s', forward='%s'" \
               ", reverse='%s', light on='%s', warning='%s', daytime='%s')>" \
               % ((self.frame_id, self.frame_value) + tuple(self.switches_status))

    # Updates the gui values
    def update_gui(self, gui_interface: GUIInterface) -> None:
        gui_interface.update_switches(switches_status=self.switches_status)