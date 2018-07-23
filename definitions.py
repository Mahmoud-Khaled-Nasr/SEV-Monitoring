from enum import Enum

class Constants:
    BASE_MASTER_MOTOR_CURRENT = 100
    BASE_SLAVE_MOTOR_CURRENT = 100

class ConnectionTypes(Enum):
    USB = 1
    WIFI = 2


# Normal ranges for all types of data (min, max)
class Ranges:
    battery_current = (100, 200)
    motors_current = (100, 200)
    solar_panels_current = (100, 200)

    x_volt = (100, 200)
    dc_bus_volt = (100, 200)

    x_temperature = (100, 200)
    y_temperature = (100, 200)
    solar_panels_temperature = (100, 200)

    min_battery_volt = (100, 200)
    max_battery_volt = (100, 200)
    max_battery_temperature = (100, 200)

    master_motor_current = (100, 200)
    master_motor_speed = (100, 200)

    slave_motor_current = (100, 200)
    slave_motor_speed = (100, 200)

    battery_module_volt = (100, 200)
    battery_module_temperature = (100, 200)


# Tolerance for all types of data
# Only changes beyond the tolerance are shown on the gui
class Tolerances:
    battery_current = 100
    motors_current = 100
    solar_panels_current = 100

    x_volt = 100
    dc_bus_volt = 100

    x_temperature = 100
    y_temperature = 100
    solar_panels_temperature = 100

    min_battery_volt = 100
    max_battery_volt = 100
    max_battery_temperature = 100

    master_motor_current = 100
    master_motor_speed = 100

    slave_motor_current = 100
    slave_motor_speed = 100

    battery_module_volt = 100
    battery_module_temperature = 100


class IDs:
    CURRENTS_FRAME_ID = 320
    BUS_VOLTAGES_FRAME_ID = 272
    TEMPERATURES_FRAME_ID = 368
    BATTERIES_FRAMES_IDS = [640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 656, 657, 658, 659]
    LIGHTS_FRAME_ID = 10
    SWITCHES_FRAME_ID = 11
    DRIVER_MASTER_MC_FRAME_ID = 1345
    DRIVER_SLAVE_MC_FRAME_ID = 1409


class DatabaseTablesNames:
    DATA_FRAME_TABLE = "data_frames"
    CURRENT_TABLE = "currents"
    BUS_VOLTAGE_TABLE = "bus_voltages"
    TEMPERATURE_TABLE = "temperatures"
    BATTERY_TABLE = "batteries"
    LIGHT_TABLE = "lights"
    SWITCH_TABLE = "switches"
    DRIVER_MASTER_MC_TABLE = "master_mc"
    DRIVER_SLAVE_MC_TABLE = "slave_mc"
