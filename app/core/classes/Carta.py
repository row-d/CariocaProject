from typing import List
from core.enums.Pinta import Pinta
from core.enums.ValorDeCarta import ValorDeCarta
from core.enums.Color import Color


class Carta:
    def __init__(self, pinta: Pinta, valor: ValorDeCarta, color: Color) -> None:
        self.pinta = pinta
        self.valor = valor
        self.color = color

    def __str__(self) -> str:
        return f"{self.valor.name},{self.pinta.name},\33[{self.color.value}m{self.color.name}\33[0m"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Carta):
            raise TypeError(
                "El parámetro __o debe ser una instancia de la clase Carta")
        return self.pinta == __o.pinta and self.valor == __o.valor and self.color == __o.color
    # overload "+" operator

    def __add__(self, __o: object) -> int:
        if isinstance(__o, int):
            return self.valor.value + __o

        if not isinstance(__o, Carta):
            raise TypeError(
                "El parámetro __o debe ser una instancia de la clase Carta")
        return self.valor.value + __o.valor.value


Cartas = List[Carta]
Baja = List[Cartas]


def str_a_carta(cadena: str) -> Carta:
    if not isinstance(cadena, str):
        raise TypeError("El parámetro cadena debe ser un string")
    if len(cadena.split(",")) != 3:
        raise ValueError(
            "El parámetro cadena debe tener el formato: valor,pinta,color")
    valor, pinta, color = cadena.split(",")
    return Carta(pinta=Pinta[pinta], valor=ValorDeCarta[valor], color=Color[color])


def str_a_cartas(cadena: str) -> Cartas:
    if not isinstance(cadena, str):
        raise TypeError("El parámetro cadena debe ser un string")
    return [str_a_carta(carta) for carta in cadena.split(" ")]
