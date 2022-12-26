from random import shuffle

from core.classes.PilaDeCartas import PilaDeCartas


class Mazo(PilaDeCartas):
    def __init__(self):
        super().__init__()

    def desordenar(self):
        shuffle(self.cartas)
