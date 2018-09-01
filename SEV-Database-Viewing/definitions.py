from enum import Enum


# Motors currents base values to convert read percentages to absolute values
class CurrentsBaseValues:
    MASTER_MOTOR_CURRENT = 100
    SLAVE_MOTOR_CURRENT = 100


# Types of connections from the car to the PC
class ConnectionTypes(Enum):
    USB = 1
    WIFI = 2


# Normal ranges for all types of data (min, max)
# Values outside the ranges are highlighted in the GUI
class Ranges:
    BATTERY_CURRENT = (100, 200)
    MOTORS_CURRENT = (100, 200)
    SOLAR_PANELS_CURRENT = (100, 200)

    CHARGE_RATE = (100, 200)
    DC_BUS_VOLT = (100, 200)

    SOLAR_PANELS_TEMPERATURE = (100, 200)

    MIN_BATTERY_VOLT = (100, 200)
    MAX_BATTERY_VOLT = (100, 200)
    MAX_BATTERY_TEMPERATURE = (100, 200)

    MASTER_MOTOR_CURRENT = (100, 200)
    MASTER_MOTOR_SPEED = (100, 200)

    SLAVE_MOTOR_CURRENT = (100, 200)
    SLAVE_MOTOR_SPEED = (100, 200)

    BATTERY_MODULE_VOLT = (100, 200)
    BATTERY_MODULE_TEMPERATURE = (100, 200)


# Tolerance for all types of data
# Only changes beyond the tolerance are shown on the gui
class Tolerances:
    BATTERY_CURRENT = 100
    MOTORS_CURRENT = 100
    SOLAR_PANELS_CURRENT = 100

    CHARGE_RATE = 100
    DC_BUS_VOLT = 100

    SOLAR_PANELS_TEMPERATURE = 100

    MIN_BATTERY_VOLT = 100
    MAX_BATTERY_VOLT = 100
    MAX_BATTERY_TEMPERATURE = 100

    MASTER_MOTOR_CURRENT = 100
    MASTER_MOTOR_SPEED = 100

    SLAVE_MOTOR_CURRENT = 100
    SLAVE_MOTOR_SPEED = 100

    BATTERY_MODULE_VOLT = 100
    BATTERY_MODULE_TEMPERATURE = 100

    
# Data frames ids in decimal form
class DataFramesIDs:
    CURRENTS_FRAME_ID = 320
    BUS_VOLTAGES_FRAME_ID = 272
    TEMPERATURES_FRAME_ID = 368
    MODULES_FRAME_IDS = [640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 656, 657, 658, 659]
    LIGHTS_FRAME_ID = 10
    SWITCHES_FRAME_ID = 11
    DRIVER_MASTER_MC_FRAME_ID = 1345
    DRIVER_SLAVE_MC_FRAME_ID = 1409


# Names for the database tables of data frames
# TODO refactor
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


# Types of database tables
class DatabaseTableTypes(Enum):
    DATA_FRAME_TABLE = 0
    CURRENTS_TABLE = 1
    BUS_VOLTAGES_TABLE = 2
    TEMPERATURES_TABLE = 3
    BATTERIES_TABLE = 4
    MASTER_MOTOR_TABLE = 5
    SLAVE_MOTOR_TABLE = 6
    LIGHTS_TABLE = 7
    SWITCHES_TABLE = 8


# All monitored items
class MonitoredItems(Enum):
    BATTERY_CURRENT = 1
    MOTORS_CURRENT = 2
    SOLAR_PANELS_CURRENT = 3

    CHARGE_RATE = 4
    DC_BUS_VOLT = 5

    SOLAR_PANELS_TEMPERATURE = 6

    MIN_BATTERY_VOLT = 7
    MAX_BATTERY_VOLT = 8
    MAX_BATTERY_TEMPERATURE = 9

    MASTER_MOTOR_CURRENT = 10
    MASTER_MOTOR_SPEED = 11

    SLAVE_MOTOR_CURRENT = 12
    SLAVE_MOTOR_SPEED = 13

    BATTERY_MODULE_VOLT = 14
    BATTERY_MODULE_TEMPERATURE = 15