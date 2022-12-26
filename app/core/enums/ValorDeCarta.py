from enum import IntEnum


class ValorDeCarta(IntEnum):
    """
    Enumeración de los valores de las cartas.
    Ejemplos de uso:
      ValorDeCarta(2)
      ValorDeCarta.K
      ValorDeCarta(13)
      ValorDeCarta['K']
    """
    2
    3
    4
    5
    6
    7
    8
    9
    10
    J = 11
    Q = 12
    K = 13
