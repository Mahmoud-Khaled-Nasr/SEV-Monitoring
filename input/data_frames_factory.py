from struct import unpack

from definitions import DataFramesIDs
from models.data_frames.data_frame import DataFrame
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.battery_data_frame import BatteryDataFrame
from models.data_frames.driver_master_MC_data_frame import DriverMasterMCDataFrame
from models.data_frames.driver_slave_MC_data_frame import DriverSlaveMCDataFrame
from models.data_frames.lights_status_data_frame import LightsDataFrame
from models.data_frames.switches_status_data_frame import SwitchesDataFrame

from typing import List


class UnknownFrameID(Exception):
    
    def __init__(self):
        super(UnknownFrameID, self).__init__("unknown Data Frame ID")


# Returns the appropriate data frame size (in bytes) according to its id
def get_data_frame_size(frame_id: int) -> int:

    # Default frame size (for unknown frame IDs)
    frame_size: int = 0
      
    if frame_id == DataFramesIDs.CURRENTS_FRAME_ID:
        frame_size = 6
    elif frame_id == DataFramesIDs.BUS_VOLTAGES_FRAME_ID:
        frame_size = 2
    elif frame_id == DataFramesIDs.TEMPERATURES_FRAME_ID:
        frame_size = 3
    elif frame_id in DataFramesIDs.MODULES_FRAME_IDS:
        frame_size = 2
    elif frame_id == DataFramesIDs.LIGHTS_FRAME_ID:
        frame_size = 1
    elif frame_id == DataFramesIDs.SWITCHES_FRAME_ID:
        frame_size = 1
    elif frame_id == DataFramesIDs.DRIVER_MASTER_MC_FRAME_ID:
        frame_size = 8
    elif frame_id == DataFramesIDs.DRIVER_SLAVE_MC_FRAME_ID:
        frame_size = 8
    else:
        raise UnknownFrameID

    return frame_size


def create_data_frame_object(frame_id, frame_value: bytes) -> DataFrame:

    if frame_id == DataFramesIDs.CURRENTS_FRAME_ID:
        parsing_string = "<HHH"
        (battery_current, motors_current, solar_panels_current) = unpack(parsing_string, frame_value)
        return CurrentsDataFrame(frame_id=frame_id, frame_value=frame_value, battery_current=battery_current,
                                 motors_current=motors_current, solar_panels_current=solar_panels_current)
    elif frame_id == DataFramesIDs.BUS_VOLTAGES_FRAME_ID:
        parsing_string = "<HH"
        (DC_bus_voltage, charge_rate) = unpack(parsing_string, frame_value)
        return BusVoltagesDataFrame(frame_id=frame_id, frame_value=frame_value, DC_bus_voltage=DC_bus_voltage)
    elif frame_id == DataFramesIDs.TEMPERATURES_FRAME_ID:
        parsing_string = "<h"
        (solar_panels_temperature) = unpack(parsing_string, frame_value)
        return TemperaturesDataFrame(frame_id=frame_id, frame_value=frame_value,
                                     solar_panels_temperature=solar_panels_temperature)
    elif frame_id in DataFramesIDs.MODULES_FRAME_IDS:
        parsing_string = "<Hh"
        (voltage, temperature) = unpack(parsing_string, frame_value)
        return BatteryDataFrame(frame_id=frame_id, frame_value=frame_value)
    elif frame_id == DataFramesIDs.LIGHTS_FRAME_ID:
        # each bit represents the status of one of the lights
        headlights: bool = 0b00000001 & frame_value[0] != 0
        tail_lights: bool = 0b00000010 & frame_value[0] != 0
        left_indicator: bool = 0b00000100 & frame_value[0] != 0
        right_indicator: bool = 0b00001000 & frame_value[0] != 0
        high_beam: bool = 0b00010000 & frame_value[0] != 0
        brake_light: bool = 0b00100000 & frame_value[0] != 0
        backing_light: bool = 0b01000000 & frame_value[0] != 0
        daytime_light: bool = 0b10000000 & frame_value[0] != 0

        return LightsDataFrame(frame_id=frame_id, frame_value=frame_value, headlights=headlights,
                               tail_lights=tail_lights, left_indicator=left_indicator,
                               right_indicator=right_indicator, high_beam=high_beam,
                               brake_light=brake_light, backing_light=backing_light,
                               daytime_light=daytime_light)

    elif frame_id == DataFramesIDs.SWITCHES_FRAME_ID:
        # each bit represents the status of one of the switches
        motor_on: bool = 0b00000001 & frame_value[0] != 0
        forward: bool = 0b00000010 & frame_value[0] != 0
        reverse: bool = 0b00000100 & frame_value[0] != 0
        light_on: bool = 0b00001000 & frame_value[0] != 0
        warning: bool = 0b00010000 & frame_value[0] != 0
        daytime: bool = 0b00100000 & frame_value[0] != 0

        return SwitchesDataFrame(frame_id=frame_id, frame_value=frame_value, motor_on=motor_on,
                                 forward=forward, reverse=reverse, light_on=light_on, warning=warning,
                                 daytime=daytime)

    elif frame_id == DataFramesIDs.DRIVER_MASTER_MC_FRAME_ID:
        # TODO which frame is this?? and reimplement this segment when the new data frames arrives
        # TODO calculate current from current percentage using costants in definitions
        parsing_string = "<HH"
        return DriverMasterMCDataFrame(frame_id=frame_id, frame_value=frame_value)
    elif frame_id == DataFramesIDs.DRIVER_SLAVE_MC_FRAME_ID:
        # TODO which frame is this?? and reimplement this segment when the new data frames arrives
        # TODO calculate current from current percentage using constants in definitions
        parsing_string = "<HH"
        return DriverSlaveMCDataFrame(frame_id=frame_id, frame_value=frame_value)
