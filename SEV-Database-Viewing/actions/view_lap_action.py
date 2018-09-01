from database.database import Session
from actions.action import Action
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.lights_status_data_frame import LightsDataFrame
from models.data_frames.switches_status_data_frame import SwitchesDataFrame
from models.laps.lap import Lap


class ViewLapAction(Action):
    # Constructor
    def __init__(self, dispatcher, lap_id: int):
        super().__init__(dispatcher)
        session = Session()
        self.lap: Lap = session.query(Lap).filter_by(id = lap_id).all()[0]  # Should return a list containing one Lap
        session.close()
        # print(self.lap)

    def execute(self):
        self.dispatcher.current_lap = self.lap
        # Todo add initial settings
