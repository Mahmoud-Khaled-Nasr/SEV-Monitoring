from abc import ABCMeta, abstractmethod

from dispatcher import Dispatcher


class Action(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher: Dispatcher = dispatcher

    @abstractmethod
    def execute(self):
        pass
