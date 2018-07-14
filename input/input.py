from PyQt5.QtCore import QThread, pyqtSignal
from serial import Serial
from models.data_frames.data_frame import DataFrame


class SerialInterface(QThread):
    signal_receive_serial_data = pyqtSignal(DataFrame)

    def __init__(self, com_port: str, baud_rate: int):
        super(SerialInterface, self).__init__()
        self.COM = com_port
        self.baud_rate = baud_rate
        self.serial = None

    def run(self):
        self.serial = Serial(self.COM, self.baud_rate)
        while True:
            frame_id = self.get_frame_id()
            frame_data = self.get_frame_data(frame_id)
            frame = DataFrame(frame_id, frame_data)
            self.signal_receive_serial_data.emit(frame)

    def get_frame_id(self) -> int:
        pass

    def get_frame_data(self, frame_id: int) -> bytes:
        pass
