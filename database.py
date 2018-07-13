from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DatabaseBaseClass = declarative_base()
database_engine = create_engine('sqlite:///monitoring.db', echo=True)

# Import the models here to be created by the database
from models.data_frames.data_frame import DataFrame
from models.laps.lap import Lap

# Database initialization
DatabaseBaseClass.metadata.create_all(database_engine)
print(database_engine)

Session = sessionmaker(bind=database_engine)

database_session: Session = Session()
