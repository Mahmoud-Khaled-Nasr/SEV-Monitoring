from socket import socket, SOCK_DGRAM, AF_INET
from typing import Callable, List

from PyQt5.QtCore import QThread, pyqtSignal

from input.data_frames_factory import get_data_frame_size, create_data_frame_object, unpack_raw_id\
    , STARTING_SEQUENCE, TERMINATING_SEQUENCE, FRAME_ID_SIZE
from models.data_frames.data_frame import DataFrame


class WiFiReader(QThread):

    signal_receive_wifi_data: pyqtSignal = pyqtSignal(DataFrame)

    # The size of the receive buffer
    BROADCAST_BUFFER_SIZE: int = 256

    def __init__(self, broadcase_IP: str, broadcast_port: int, server_IP: str, server_port: int):
        super(WiFiReader, self).__init__()

        self.broadcase_IP = broadcase_IP
        self.broadcast_port = broadcast_port
        self.server_IP = server_IP
        self.server_port = server_port

        self.operate = True

        self.input_data_buffer: bytes = b''

        # socket connection to the UDP server
        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        self.server_socket.settimeout(None)

        # socket that receive the broadcast data
        self.broadcast_socket = socket(AF_INET, SOCK_DGRAM)
        self.broadcast_socket.setblocking(True)

    def run(self):
        self.__open_broadcast_socket()
        self.__open_client_socket()
        self.__start_communication()
        while self.operate:
            packet = self.broadcast_socket.recv(self.BROADCAST_BUFFER_SIZE)
            print(packet)
            data_frames_list: List[DataFrame] = self.__parse_packet(packet)
            for data_frame in data_frames_list:
                self.signal_receive_wifi_data.emit(data_frame)

        self.__end_communication()
        self.server_socket.close()
        self.broadcast_socket.close()

    def stop(self):
        self.operate = False

    def connect_receive_data_signal(self, receive_data_slot: Callable):
        self.signal_receive_wifi_data.connect(receive_data_slot)

    def __open_broadcast_socket(self):
        self.broadcast_socket.bind((self.server_IP, self.broadcast_port))

    def __open_client_socket(self):
        self.server_socket.connect((self.server_IP, self.server_port))

    def __start_communication(self):
        self.server_socket.send(STARTING_SEQUENCE)
        m = self.server_socket.recv(256)
        print(m)

    def __end_communication(self):
        self.server_socket.send(TERMINATING_SEQUENCE)
        m = self.server_socket.recv(256)
        print(m)

    def __parse_packet(self, packet: bytes) -> List[DataFrame]:
        packet_size: int = len(self.input_data_buffer)
        index: int = 0
        data_frames_list: List[DataFrame] = []
        # Loop the frames one by one and parse it
        while index < packet_size:
            frame_id: int = unpack_raw_id(packet[index:index + FRAME_ID_SIZE])
            index += FRAME_ID_SIZE
            frame_size: int = get_data_frame_size(frame_id)
            frame_raw_data: bytes = packet[index:index + frame_size]
            index += frame_size
            frame_object: DataFrame = create_data_frame_object(frame_id, frame_raw_data)
            data_frames_list.append(frame_object)
            # for testing
            print(frame_id)
            print(frame_raw_data)

        return data_frames_list
