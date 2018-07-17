from struct import unpack
from definitions import IDs
from PyQt5.QtCore import QThread, pyqtSignal
from serial import Serial, SerialException
from models.data_frames.data_frame import DataFrame
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.battery_data_frame import BatteryDataFrame
from models.data_frames.driver_master_MC_data_frame import DriverMasterMCDataFrame
from models.data_frames.driver_slave_MC_data_frame import DriverSlaveMCDataFrame
from models.data_frames.lights_status_data_frame import LightsDataFrame
from models.data_frames.switches_status_data_frame import SwitchesDataFrame
from typing import Callable


class SerialReader(QThread):

    signal_receive_serial_data = pyqtSignal(DataFrame)

    FRAME_ID_SIZE: int = 2
    STARTING_SEQUENCE: bytes = b'0xff'
    TERMINATING_SEQUENCE: bytes = b'0x11'

    def __init__(self, com_port: str, baud_rate: int):
        super(SerialReader, self).__init__()
        self.COM: str = com_port
        self.baud_rate: int = baud_rate
        self.serial: Serial = None
        self.isStopped = False

    def run(self):
        try:
            self.serial = Serial(port=self.COM, baudrate=self.baud_rate)
            # the serial will write to the micro controller to start sending the data
            self.serial.write(self.STARTING_SEQUENCE)
            # Reading loop
            while not self.isStopped:
                # Get frame id
                frame_id: int = self.__get_frame_id()
                # Get frame data
                frame_data: bytes = self.__get_frame_data(frame_id)
                # Create the frame
                frame = self.__create_frame(frame_id, frame_data)
                # Emit a signal
                self.signal_receive_serial_data.emit(frame)

            self.serial.write(self.TERMINATING_SEQUENCE)
            self.serial.close()

        except SerialException:
            print("Could not read from the port")

    def __get_frame_id(self) -> int:
        _FRAME_ID_PARSING_STRING = ">h"
        # read the first 2 bytes from serial for the frame id convert them using unpack to int and return it
        return unpack(_FRAME_ID_PARSING_STRING, self.serial.read(size=self.FRAME_ID_SIZE))[0]

    def __get_frame_data(self, frame_id: int) -> bytes:
        # TODO see if u will need the frame id or not
        # The value of the id may be used to make the communication more efficient by 50%
        return self.serial.read(8)

    def __create_frame(self, frame_id: int, frame_data: bytes) -> DataFrame:
        # Currents Frame
        if frame_id == IDs.currents_frame_id:
            return CurrentsDataFrame(frame_id, frame_data)
        # Bus Voltages Frame
        elif frame_id == IDs.bus_voltages_frame_id:
            return BusVoltagesDataFrame(frame_id, frame_data)
        # Temperatures Frame
        elif frame_id == IDs.temperatures_frame_id:
            return TemperaturesDataFrame(frame_id, frame_data)
        # Driver Master MC Frame
        elif frame_id == IDs.driver_master_mc_frame_id:
            return DriverMasterMCDataFrame(frame_id, frame_data)
        # Driver Slave MC Frame
        elif frame_id == IDs.driver_slave_mc_frame_id:
            return DriverSlaveMCDataFrame(frame_id, frame_data)
        # Lights Frame
        elif frame_id == IDs.lights_frame_id:
            return LightsDataFrame(frame_id, frame_data)
        # Switches Frame
        elif frame_id == IDs.switches_frame_id:
            return SwitchesDataFrame(frame_id, frame_data)
        # Battery Frame
        elif frame_id in IDs.modules_frame_ids:
            # Get the module number
            module_number = IDs.modules_frame_ids.index(frame_id) + 1
            return BatteryDataFrame(frame_id, frame_data, module_number)

    def stop_reading(self) -> None:
        self.isStopped = True

    def connect_receive_data_signal(self, receive_data_slot: Callable):
        self.signal_receive_serial_data.connect(receive_data_slot)