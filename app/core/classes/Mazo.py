from random import shuffle

from core.classes.PilaDeCartas import PilaDeCartas
from core.classes.Carta import Cartas


class Mazo(PilaDeCartas):
    def __init__(self, cartas: Cartas = []):
        super().__init__(cartas=cartas)

    def desordenar(self):
        shuffle(self.cartas)
