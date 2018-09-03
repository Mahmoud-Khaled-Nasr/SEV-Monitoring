from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DatabaseBaseClass = declarative_base()
database_engine = create_engine('sqlite:///monitoring.db', echo=True)

# Import the models here to be created by the database
from models.data_frames.data_frame import DataFrame
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.battery_data_frame import BatteryDataFrame
from models.data_frames.lights_status_data_frame import LightsDataFrame
from models.data_frames.switches_status_data_frame import SwitchesDataFrame
from models.data_frames.driver_master_MC_data_frame import DriverMasterMCDataFrame
from models.data_frames.driver_slave_MC_data_frame import DriverSlaveMCDataFrame
from models.laps.lap import Lap

# Database initialization
DatabaseBaseClass.metadata.create_all(database_engine)
print(database_engine)

Session = sessionmaker(bind=database_engine)

from database.insert_data_frame import InsertDataFrames

insert_data_frames = InsertDataFrames()

from database.database_seed import seed_database

seed_database()
