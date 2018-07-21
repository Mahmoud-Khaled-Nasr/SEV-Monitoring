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
from models.laps.lap import Lap

# Database initialization
DatabaseBaseClass.metadata.create_all(database_engine)
print(database_engine)

Session = sessionmaker(bind=database_engine)

database_session: Session = Session()
