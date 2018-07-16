from struct import unpack

from PyQt5.QtCore import QThread, pyqtSignal
from serial import Serial
from models.data_frames.data_frame import DataFrame
from models.data_frames.current_data_frame import CurrentDataFrame


class SerialInterface(QThread):

    signal_receive_serial_data = pyqtSignal(DataFrame)

    FRAME_ID_SIZE: int = 2
    STARTING_SEQUENCE: bytes = b'0xff'
    TERMINATING_SEQUENCE: bytes = b'0x11'

    def __init__(self, com_port: str, baud_rate: int):
        super(SerialInterface, self).__init__()
        self.COM: str = com_port
        self.baud_rate: int = baud_rate
        self.serial: Serial = None

    def run(self):
        self.serial = Serial(port=self.COM, baudrate=self.baud_rate)
        # the serial will write to the micro controller to start sending the data
        self.serial.write(self.STARTING_SEQUENCE)
        while True:
            frame_id: int = self.get_frame_id()
            frame_data: bytes = self.get_frame_data(frame_id)
            # TODO Yosry implement this
            '''
                if frame_id = CURRENT_FRAME_ID:  ==> which is a const defined somewhere with the frame id from the can
                    frame: CurrentDataFrame(frame_id, frame_data)
                elif frame_id = OTHER_ID 
                    frame: OtherFrame(frame_id, frame_data)
                elif frame_id = other_id2 
                
                and so on the frame ids will be saved here as constants u will get them from the excel file
                then u will emit it at the end
            '''
            self.signal_receive_serial_data.emit(frame)

    def get_frame_id(self) -> int:
        _FRAME_ID_PARSING_STRING = ">h"
        # read the first 2 bytes from serial for the frame id convert them using unpack to int and return it
        return unpack(_FRAME_ID_PARSING_STRING, self.serial.read(size=self.FRAME_ID_SIZE))[0]

    def get_frame_data(self, frame_id: int) -> bytes:
        # TODO see if u will need the frame id or not
        # The value of the id may be used to make the communication more efficient by 50%
        return self.serial.read(8)

    def terminate_serial_connection(self) -> None:
        self.serial.write(self.TERMINATING_SEQUENCE)
        self.serial.close()
