from database.database import Session
from lap_viewer.actions.action import Action
from models.laps.lap import Lap
from models.data_frames.data_frame import DataFrame


# Action for deleting a lap from the database
class DeleteLapAction(Action):
    # Constructor
    def __init__(self, dispatcher, lap_id: int):
        super().__init__(dispatcher)
        self.lap_id = lap_id

    def execute(self):
        # Open a session to the database
        session: Session = Session()
        # Query the lap by its id
        laps = session.query(Lap).filter_by(id=self.lap_id).all()  # Should return a list containing one Lap
        if laps:  # Making sure the list returned isn't empty
            # Delete data from all data frames tables (subclasses of DataFrame )
            '''
            session.query(table).filter(table.lap_id == self.lap_id).delete()
            Can't be used as lap_id column exists in the Data Frames table.
            Delete statements cannot be executed with conditions from multiple tables.
            
            Individual data frame tables data have to be deleted, deleting data in data frames table doesn't
            delete all data in the individual tables.
            '''
            tables = DataFrame.__subclasses__()  # All individual frames tables
            for table in tables:
                data_to_delete = session.query(table).filter(table.lap_id == self.lap_id).all()
                print(table)
                print("data to delete")
                print(data_to_delete)
                for data_row in data_to_delete:
                    # Data has to be deleted object by object
                    session.delete(data_row)
            # Delete the lap from the laps table
            session.query(Lap).filter(Lap.id == self.lap_id).delete()
        # Commit changes to the database and close the session
        session.commit()
        session.close()
