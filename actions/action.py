from abc import ABCMeta, abstractmethod

from dispatcher import Dispatcher


class Action(object):

    __metaclass__ = ABCMeta
    __gui = None

    @abstractmethod
    def __init__(self, dispatcher: Dispatcher):
        self.__dispatcher = dispatcher

    @abstractmethod
    def execute(self):
        pass
