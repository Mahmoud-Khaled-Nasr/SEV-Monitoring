from abc import ABCMeta, abstractmethod

from dispatcher import Dispatcher


class Action(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    @abstractmethod
    def execute(self):
        pass
