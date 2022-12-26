from core.enums.Pinta import Pinta
from core.enums.ValorDeCarta import ValorDeCarta
from core.enums.Color import Color


class Carta:
    def __init__(self, pinta: int, valor: int, color: int) -> None:
        self.pinta = pinta
        self.valor = valor
        self.color = color
