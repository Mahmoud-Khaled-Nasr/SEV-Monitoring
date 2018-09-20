from abc import ABCMeta, abstractmethod


# Abstract class for all the actions classes.
class Action(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    @abstractmethod
    def execute(self):
        pass
