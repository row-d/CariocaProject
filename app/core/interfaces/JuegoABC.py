from core.lib.event import EventEmitter
from abc import ABCMeta


class Juego(EventEmitter, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @property
    def actualRound(self):
        raise NotImplementedError("actualRound property not implemented")

    @property
    def table(self):
        raise NotImplementedError("table property not implemented")

    @classmethod
    def start(self):
        raise NotImplementedError("start method not implemented")

    @classmethod
    def stop(self):
        raise NotImplementedError("stop method not implemented")

    @classmethod
    def menu(self):
        raise NotImplementedError("menu method not implemented")
