import os
from random import random, randint, getrandbits

from database.database import Session
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.battery_data_frame import BatteryDataFrame
from models.data_frames.lights_status_data_frame import LightsDataFrame
from models.data_frames.switches_status_data_frame import SwitchesDataFrame
from models.laps.lap import Lap
from definitions import DataFramesIDs as df_ids
from definitions import Ranges as ranges


def seed_database():
    # check if seeding is needed
    database_session: Session = Session()
    if database_session.query(Lap).count() != 0:
        database_session.close()
        return

    LAPS_NUMBER: int = 10
    FRAMES_NUMBER_PER_FRAME_TYPE: int = 30
    LAP_NAME: str = "Name"

    for i in range(0, LAPS_NUMBER):
        lap: Lap = Lap(LAP_NAME + str(i))
        database_session.add(lap)
        for j in range(0, FRAMES_NUMBER_PER_FRAME_TYPE):
            df1: CurrentsDataFrame = CurrentsDataFrame(df_ids.CURRENTS_FRAME_ID
                                                       , os.urandom(8)
                                                       , randint(ranges.BATTERY_CURRENT[0], ranges.BATTERY_CURRENT[1])
                                                       , randint(ranges.MOTORS_CURRENT[0], ranges.MOTORS_CURRENT[1])
                                                       , randint(ranges.SOLAR_PANELS_CURRENT[0]
                                                                , ranges.SOLAR_PANELS_CURRENT[1]))
            df2: BusVoltagesDataFrame = BusVoltagesDataFrame(df_ids.BUS_VOLTAGES_FRAME_ID
                                                             , os.urandom(8)
                                                             , 100#randint(ranges.DC_BUS_VOLT[0], ranges.DC_BUS_VOLT[1])
                                                             , randint(ranges.CHARGE_RATE[0], ranges.CHARGE_RATE[1]))
            df3: TemperaturesDataFrame = TemperaturesDataFrame(df_ids.TEMPERATURES_FRAME_ID
                                                               , os.urandom(8)
                                                               , randint(ranges.SOLAR_PANELS_TEMPERATURE[0]
                                                                        , ranges.SOLAR_PANELS_TEMPERATURE[1]))
            # TODO seed the battery table
            df5: LightsDataFrame = LightsDataFrame(df_ids.LIGHTS_FRAME_ID
                                                   , os.urandom(8)
                                                   , bool(getrandbits(1))
                                                   , bool(getrandbits(1))
                                                   , bool(getrandbits(1))
                                                   , bool(getrandbits(1))
                                                   , bool(getrandbits(1))
                                                   , bool(getrandbits(1))
                                                   , bool(getrandbits(1))
                                                   , bool(getrandbits(1)))
            df6: SwitchesDataFrame = SwitchesDataFrame(df_ids.SWITCHES_FRAME_ID
                                                       , os.urandom(8)
                                                       , bool(getrandbits(1))
                                                       , bool(getrandbits(1))
                                                       , bool(getrandbits(1))
                                                       , bool(getrandbits(1))
                                                       , bool(getrandbits(1))
                                                       , bool(getrandbits(1)))
            lap.finish_lap()
            df1.lap = lap
            df2.lap = lap
            df3.lap = lap
            df5.lap = lap
            df6.lap = lap
            database_session.add(df1)
            database_session.add(df2)
            database_session.add(df3)
            database_session.add(df5)
            database_session.add(df6)

    database_session.commit()
    database_session.close()
