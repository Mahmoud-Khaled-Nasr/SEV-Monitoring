from input.serial_reader import SerialReaderThread


class SerialInterface:
    def __init__(self, com_port: str, baud_rate: int):
        self.serial_reader = SerialReaderThread(com_port, baud_rate)
        self.signal_receive_serial_data = self.serial_reader.signal_receive_serial_data

    def start(self):
        self.serial_reader.start()

    def terminate(self):
        self.serial_reader.terminate_serial_connection()
        self.serial_reader.terminate()