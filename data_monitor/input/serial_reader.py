import time

from PyQt5.QtCore import QThread, pyqtSignal
from serial import Serial, SerialException
from typing import Callable

from data_monitor.input.data_frames_factory import get_data_frame_size, create_data_frame_object, unpack_raw_id\
    , STARTING_SEQUENCE, TERMINATING_SEQUENCE, FRAME_ID_SIZE
from models.data_frames.data_frame import DataFrame


class SerialReader(QThread):

    signal_receive_serial_data = pyqtSignal(DataFrame)

    def __init__(self, com_port: str, baud_rate: int):
        super(SerialReader, self).__init__()
        self.COM: str = com_port
        self.baud_rate: int = baud_rate
        self.serial: Serial = None
        # TODO test the idea of boolean
        self.operate: bool = True

    def run(self):
        self.operate = True
        try:
            print("reading started")  # For testing
            self.serial = Serial(port=self.COM, baudrate=self.baud_rate)
            self.serial.reset_input_buffer()
            self.serial.reset_output_buffer()
            if self.serial.is_open:
                print("the port is open")
            else:
                print("the port is not open")
            # serial will signal the micro controller to start sending the data
            time.sleep(3)
            self.serial.write(STARTING_SEQUENCE)
            # Reading loop
            while self.operate:
                # Get frame id
                raw_id: bytes = self.__get_frame_id()
                frame_id: int = unpack_raw_id(raw_id)
                print(frame_id)
                # Get data frame size
                frame_size: int = get_data_frame_size(frame_id)
                # Get frame data
                frame_data: bytes = self.__get_frame_data(frame_size)
                # Create the frame
                frame_object: DataFrame = create_data_frame_object(frame_id, frame_data)
                # Emit a signal
                self.signal_receive_serial_data.emit(frame_object)

            # Check that the serial object was successfully created
            if self.serial:
                # serial will signal the micro controller to stop sending the data
                self.serial.write(TERMINATING_SEQUENCE)
                # Close the port
                self.serial.close()
            print("reading stopped")  # For testing

        except SerialException:
            # serial object wasn't successfully created
            # Could not open port
            print("Could not read from the port")

    def __get_frame_id(self) -> bytes:
        raw_id: bytes = self.serial.read(FRAME_ID_SIZE)
        # read the first 2 bytes from serial for the frame id convert them using unpack to int and return it
        return raw_id

    def __get_frame_data(self, frame_size: int) -> bytes:
        return self.serial.read(frame_size)

    def stop(self):
        self.operate = False

    def connect_receive_data_signal(self, receive_data_slot: Callable):
        self.signal_receive_serial_data.connect(receive_data_slot)
