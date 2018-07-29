from struct import unpack

from definitions import IDs
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

    if frame_id == IDs.CURRENTS_FRAME_ID:
        frame_size = 6

    elif frame_id == IDs.BUS_VOLTAGES_FRAME_ID:
        frame_size = 2

    elif frame_id == IDs.TEMPERATURES_FRAME_ID:
        frame_size = 3

    elif frame_id in IDs.BATTERIES_FRAMES_IDS:
        frame_size = 2

    elif frame_id == IDs.LIGHTS_FRAME_ID:
        frame_size = 1

    elif frame_id == IDs.SWITCHES_FRAME_ID:
        frame_size = 1

    elif frame_id == IDs.DRIVER_MASTER_MC_FRAME_ID:
        frame_size = 8

    elif frame_id == IDs.DRIVER_SLAVE_MC_FRAME_ID:
        frame_size = 8
    else:
        raise UnknownFrameID

    return frame_size


def create_data_frame_object(frame_id, frame_value: bytes) -> DataFrame:

    if frame_id == IDs.CURRENTS_FRAME_ID:
        parsing_string = "<HHH"
        (battery_current, motors_current, solar_panels_current) = unpack(parsing_string, frame_value)
        return CurrentsDataFrame(frame_id=frame_id, frame_value=frame_value, battery_current=battery_current,
                                 motors_current=motors_current, solar_panels_current=solar_panels_current)

    elif frame_id == IDs.BUS_VOLTAGES_FRAME_ID:
        parsing_string = "<HH"
        (DC_bus_voltage, dummy) = unpack(parsing_string, frame_value)
        return BusVoltagesDataFrame(frame_id=frame_id, frame_value=frame_value, DC_bus_voltage=DC_bus_voltage)

    elif frame_id == IDs.TEMPERATURES_FRAME_ID:
        parsing_string = "<hhh"
        (dummy1, solar_panels_temperature, dummy2) = unpack(parsing_string, frame_value)
        return TemperaturesDataFrame(frame_id=frame_id, frame_value=frame_value,
                                     solar_panels_temperature=solar_panels_temperature)

    elif frame_id in IDs.BATTERIES_FRAMES_IDS:
        parsing_string = "<Hh"
        (voltage, temperature) = unpack(parsing_string, frame_value)
        return BatteryDataFrame(frame_id=frame_id, frame_value=frame_value)

    elif frame_id == IDs.LIGHTS_FRAME_ID:
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

    elif frame_id == IDs.SWITCHES_FRAME_ID:
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

    elif frame_id == IDs.DRIVER_MASTER_MC_FRAME_ID:
        # TODO reimplement this segment when the new data frames arrives
        parsing_string = "<HH"
        return DriverMasterMCDataFrame(frame_id=frame_id, frame_value=frame_value)

    elif frame_id == IDs.DRIVER_SLAVE_MC_FRAME_ID:
        # TODO and reimplement this segment when the new data frames arrives
        parsing_string = "<HH"
        return DriverSlaveMCDataFrame(frame_id=frame_id, frame_value=frame_value)
