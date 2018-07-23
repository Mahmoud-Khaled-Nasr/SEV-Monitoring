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
    # Currents frame
    if frame_id == IDs.CURRENTS_FRAME_ID:
        frame_size = 6
    # Bus Voltages frame
    elif frame_id == IDs.BUS_VOLTAGES_FRAME_ID:
        frame_size = 2
    # Temperatures frame
    elif frame_id == IDs.TEMPERATURES_FRAME_ID:
        frame_size = 3
    # Battery frame
    elif frame_id in IDs.BATTERIES_FRAMES_IDS:
        frame_size = 2
    # Lights frame
    elif frame_id == IDs.LIGHTS_FRAME_ID:
        frame_size = 1
    # Switches frame
    elif frame_id == IDs.SWITCHES_FRAME_ID:
        frame_size = 1
    # Driver Master MC frame
    elif frame_id == IDs.DRIVER_MASTER_MC_FRAME_ID:
        frame_size = 8
    # Slave Master MC frame
    elif frame_id == IDs.DRIVER_SLAVE_MC_FRAME_ID:
        frame_size = 8
    else:
        raise UnknownFrameID

    return frame_size


def create_data_frame_object(frame_id, frame_value: bytes) -> DataFrame:
    # Current data frame
    if frame_id == IDs.CURRENTS_FRAME_ID:
        parsing_string = "<HHH"
        (battery_current, motors_current, solar_panels_current) = unpack(parsing_string, frame_value)
        return CurrentsDataFrame(frame_id=frame_id, frame_value=frame_value, battery_current=battery_current,
                                 motors_current=motors_current, solar_panels_current=solar_panels_current)
    # Bus Voltages data frame
    elif frame_id == IDs.BUS_VOLTAGES_FRAME_ID:
        parsing_string = "<HH"
        (DC_bus_voltage, dummy) = unpack(parsing_string, frame_value)
        return BusVoltagesDataFrame(frame_id=frame_id, frame_value=frame_value, DC_bus_voltage=DC_bus_voltage)
    # Temperatures data frame
    elif frame_id == IDs.TEMPERATURES_FRAME_ID:
        parsing_string = "<hhh"
        (dummy1, solar_panels_temperature, dummy2) = unpack(parsing_string, frame_value)
        return TemperaturesDataFrame(frame_id=frame_id, frame_value=frame_value,
                                     solar_panels_temperature=solar_panels_temperature)
    # Battery data frame
    elif frame_id in IDs.BATTERIES_FRAMES_IDS:
        parsing_string = "<Hh"
        (voltage, temperature) = unpack(parsing_string, frame_value)
        return BatteryDataFrame(frame_id=frame_id, frame_value=frame_value)
    # Lights data frame
    elif frame_id == IDs.LIGHTS_FRAME_ID:
        number_of_lights = 8
        # Create list of lights
        lights_status: List[bool] = []
        # Evaluate the bits as booleans (light status)
        compare_byte = 0b00000001
        for i in range(1, number_of_lights + 1):
            # If the bitwise comparison of the compare byte and the first (and only)
            # byte in "value" isn't equal to a zero, then the bit is 1 (corresponding to true)
            lights_status.append(frame_value[0] & compare_byte != 0)
            # Shift the compare byte to compare the next bit
            compare_byte = compare_byte << 1

        return LightsDataFrame(frame_id=frame_id, frame_value=frame_value)
    # Switches data frame
    elif frame_id == IDs.SWITCHES_FRAME_ID:
        number_of_switches = 6
        # Create list of switches
        switches_status: List[bool] = []
        # Evaluate the bits as booleans (switch status)
        compare_byte = 0b00000001
        for i in range(1, number_of_switches  + 1):
            # If the bitwise comparison of the compare byte and the first (and only)
            # byte in "value" isn't equal to a zero, then the bit is 1 (corresponding to true)
            switches_status.append(frame_value[0] & compare_byte != 0)
            # Shift the compare byte to compare the next bit
            compare_byte = compare_byte << 1

        return SwitchesDataFrame(frame_id=frame_id, frame_value=frame_value)
    # Driver Master MC data frame
    elif frame_id == IDs.DRIVER_MASTER_MC_FRAME_ID:
        # TODO reimplement this segment when the new data frames arrives
        parsing_string = "<HH"
        return DriverMasterMCDataFrame(frame_id=frame_id, frame_value=frame_value)
    # Slave Master MC data frame
    elif frame_id == IDs.DRIVER_SLAVE_MC_FRAME_ID:
        # TODO and reimplement this segment when the new data frames arrives
        parsing_string = "<HH"
        return DriverSlaveMCDataFrame(frame_id=frame_id, frame_value=frame_value)
