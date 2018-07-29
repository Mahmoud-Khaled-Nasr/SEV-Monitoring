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


class UnknownFrameID(Exception):
    
    def __init__(self):
        super(UnknownFrameID, self).__init__("unknown Data Frame ID")


def get_data_frame_size(frame_id: int) -> int:

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
        # TODO check this logic and reimplement this segment when the new data frames arrives
        number_of_lights = 8
        lights_status = []
        # Evaluate the bits as booleans (light status)
        compare_byte = 0b00000001
        for i in range(1, number_of_lights + 1):
            lights_status[i] = frame_value[0] & compare_byte
            compare_byte = compare_byte << 1

        return LightsDataFrame(frame_id=frame_id, frame_value=frame_value)

    elif frame_id == DataFramesIDs.SWITCHES_FRAME_ID:
        # TODO check this logic and reimplement this segment when the new data frames arrives
        number_of_switches = 6
        # Create list of switches
        switches_status = []
        # Evaluate the bits as booleans (switch status)
        compare_byte = 0b00000001
        for i in range(1, number_of_switches + 1):
            switches_status[i] = frame_value[0] & compare_byte
            compare_byte = compare_byte << 1

        return SwitchesDataFrame(frame_id=frame_id, frame_value=frame_value)

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
