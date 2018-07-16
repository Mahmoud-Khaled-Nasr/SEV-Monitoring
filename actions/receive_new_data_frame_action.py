from actions.action import Action
from database import database_session
from models.data_frames.data_frame import DataFrame
from models.data_frames.current_data_frame import CurrentDataFrame


class ReceiveNewDataFrameAction(Action):

    def __init__(self, dispatcher, data_frame):
        super(ReceiveNewDataFrameAction, self).__init__(dispatcher)
        self.data_frame: DataFrame = data_frame

    def execute(self):
        # the session must be used from the dispatcher but there is a problem with autocomplete till fixing it i will
        # use the object directly from the database file
        self.data_frame.lap = self.dispatcher.current_lap
        database_session.add(self.data_frame)
        database_session.commit()
        if isinstance(self.data_frame, CurrentDataFrame):
            self.dispatcher.gui_interface\
                .update_currents(battery_current=self.data_frame.battery_current
                                 , motors_current=self.data_frame.motors_current
                                 , solar_panels_current=self.data_frame.solar_panels_current)
        # TODO Yosry after implementing all the data frames classes u will check here and update the gui according to
        # the type of the object
        '''
        elif isinstance(self.data_frame, BatteryDataFrame):
            self.dispatcher.gui_interface.updateBatteriesData()
            And so on but i haven't implemented the rest yet due to problem with the types of the received data
        '''