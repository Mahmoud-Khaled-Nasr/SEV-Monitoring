from abc import ABCMeta, abstractmethod


class DataFrame:

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, frame_id: int, value: bytes):
        self.frame_id = frame_id
        self.value = value
