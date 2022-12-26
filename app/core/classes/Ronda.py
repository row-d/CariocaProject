from typing import List
from core.classes.Carta import Carta, Cartas


class Ronda:
    def __init__(self, trios: int, escalas: int) -> None:
        if trios <= 0 and escalas <= 0:
            raise ValueError(
                "Los valores de trios y escalas deben ser mayores a 0")
        self.trios = trios
        self.escalas = escalas

    def verificar_patrones(self, patrones: List[Cartas]) -> bool:
        trios = 0
        escalas = 0
        for patron in patrones:
            if self.es_trio(patron):
                trios += 1
            if self.es_escala(patron):
                escalas += 1
        return trios == self.trios and escalas == self.escalas

    @ staticmethod
    def es_trio(patron: Cartas) -> bool:
        if len(patron) != 3:
            return False
        for carta in patron:
            if carta.valor != patron[0].valor:
                return False
        return True

    @ staticmethod
    def es_escala(patron: list) -> bool:
        if len(patron) != 4:
            return False
        patron.sort(key=lambda carta: carta.valor)
        valor_actual = patron[0].valor
        for carta in range(1, len(patron)):
            if carta.valor != valor_actual + 1:
                return False
            valor_actual = carta.valor
            if carta.pinta != patron[0].pinta:
                return False
        return True


Rondas = List[Ronda]
