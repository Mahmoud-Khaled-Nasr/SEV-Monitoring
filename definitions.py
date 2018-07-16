from enum import Enum


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
