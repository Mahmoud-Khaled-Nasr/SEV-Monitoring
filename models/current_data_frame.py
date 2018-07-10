from models.data_frame import DataFrame


class CurrentDataFrame(DataFrame):

    def __init__(self, frame_id: int, value: bytes):
        super().__init__(frame_id, value)
        # each object will parse the value from bytes to the proper values for example
        self.motor_current = value[0]
        self.battery_current = value[1]
        # also the object will access the database and get the metadata of the object max, min allowed battery current
        self.get_metadata()

    def get_metadata(self):
        pass