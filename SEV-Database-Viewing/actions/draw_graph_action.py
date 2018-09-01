from database.database import Session
from actions.action import Action
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.lights_status_data_frame import LightsDataFrame
from models.data_frames.switches_status_data_frame import SwitchesDataFrame
from models.data_frames.battery_data_frame import BatteryDataFrame
from models.data_frames.driver_master_MC_data_frame import DriverMasterMCDataFrame
from models.data_frames.driver_slave_MC_data_frame import DriverSlaveMCDataFrame
from definitions import DatabaseTableTypes, MonitoredItems
from GUI.GUI_interface import GUIInterface
from typing import List


class DrawGraphAction(Action):
    # Constructor
    def __init__(self, dispatcher, items_to_draw: List[MonitoredItems]):
        super().__init__(dispatcher)
        self.items_to_draw = items_to_draw

    def execute(self):
        pass
