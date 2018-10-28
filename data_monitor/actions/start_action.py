from data_monitor.actions.action import Action
from database.database import Session
from database.database import insert_data_frames
from models.laps.lap import Lap
from definitions import ConnectionTypes


class StartAction(Action):

    def __init__(self, dispatcher, connection_type: ConnectionTypes, lap_name: str):
        super().__init__(dispatcher)
        self.connection_type = connection_type
        self.lap_name = lap_name

    def execute(self) -> None:
        # Start the serial reading thread
        self.dispatcher.current_lap = Lap(self.lap_name)
        database_session = Session()
        database_session.add(self.dispatcher.current_lap)
        database_session.commit()
        database_session.close()
        # Starting the thread that insert new frames to the database
        insert_data_frames.start()
        # Start the serial reader or wifi reader
        if self.connection_type == ConnectionTypes.USB:
            self.dispatcher.serial_reader.start()
        elif self.connection_type == ConnectionTypes.WIFI:
            self.dispatcher.wifi_reader.start()
