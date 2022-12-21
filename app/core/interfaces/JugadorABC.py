from core.lib.event import EventEmitter
from abc import ABCMeta


class JugadorABC(EventEmitter, metaclass=ABCMeta):
    def __init__(self, nombre, mano):
        pass

    @property
    def name(self):
        raise NotImplementedError("name property not implemented")

    @name.setter
    def name(self, value):
        raise NotImplementedError("name property not implemented")

    @property
    def hasCards(self):
        raise NotImplementedError("hasCards property not implemented")

    @classmethod
    def discardCard(self):
        raise NotImplementedError("discardCard method not implemented")

    @classmethod
    def takeCard(self):
        raise NotImplementedError("takeCard method not implemented")

    @classmethod
    def leaveCard(self):
        raise NotImplementedError("leaveCard method not implemented")
