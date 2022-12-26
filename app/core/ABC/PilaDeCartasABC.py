from abc import ABCMeta
from core.lib.event import EventEmitter


class PilaDeCartasABC(EventEmitter, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @classmethod
    def agregar_carta(self, carta):
        raise NotImplementedError(
            "No se ha implementado el metodo agregar_carta")

    @classmethod
    def tomar_carta(self):
        raise NotImplementedError(
            "No se ha implementado el metodo tomar_carta")

    @classmethod
    def desordenar(self):
        raise NotImplementedError(
            "No se ha implementado el metodo desordenar")
