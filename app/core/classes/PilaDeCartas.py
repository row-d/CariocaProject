from core.ABC.PilaDeCartasABC import PilaDeCartasABC


class PilaDeCartas(PilaDeCartasABC):
    def __init__(self) -> None:
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def tomar_carta(self):
        return self.cartas.pop()

    '''
    def agregar_carta(self, carta):
        pass
    def tomar_carta(self):
        pass
    def desordenar(self):
        pass
    '''
