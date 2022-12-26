from core.ABC.PilaDeCartasABC import PilaDeCartasABC
from core.classes.Carta import Carta, Cartas


class PilaDeCartas(PilaDeCartasABC):
    def __init__(self, cartas: Cartas = []) -> None:
        self.cartas = cartas

    def agregar_carta(self, carta: Carta) -> None:
        if not isinstance(carta, Carta):
            raise TypeError(
                "No se puede agregar la carta, ya que no es una instancia de Carta")
        self.cartas.append(carta)

    def tomar_carta(self) -> Carta:
        return self.cartas.pop()

    '''
    def agregar_carta(self, carta):
        pass
    def tomar_carta(self):
        pass
    def desordenar(self):
        pass
    '''
