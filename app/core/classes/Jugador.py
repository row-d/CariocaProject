from core.lib.event import EventEmitter
from core.classes.Carta import Carta


class PatronInvalido(Exception):
    def __init__(self):
        super().__init__("No se puede bajar el patron puesto que no se tiene la carta")


class NoExisteEnMano(Exception):
    def __init__(self):
        super().__init__("No se puede botar la carta ya que no se tiene en la mano")


class RecepcionManoInvalida(Exception):
    def __init__(self):
        super().__init__("No se puede recibir la mano ya que no se tiene cartas (Input vacio). ")


class Jugador(EventEmitter):
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
        self.bajas = []
        self._mano = []
        pass

    def recibir_mano(self, mano):
        if len(mano) != 0:
            self.mano = mano
        else:
            raise RecepcionManoInvalida()

    def bajar_patron(self, patron: str):
        listaPatron = [x.split(",") for x in patron.split(" ")]
        patronReal = []

        for i in range(len(listaPatron)):
            valor = listaPatron[i][0]
            pinta = listaPatron[i][1]
            color = listaPatron[i][2]
            carta_mano = self.mano[i]
            if carta_mano.valor == valor and carta_mano.pinta == pinta and carta_mano.color == color:
                patronReal.append(carta_mano)
            else:
                raise PatronInvalido()

    def botar_cartas(self, carta):
        listaCartas = carta.split(" ")
        carta_mano = []
        for i in range(len(listaCartas)):
            valor = listaCartas[i][0]
            pinta = listaCartas[i][1]
            color = listaCartas[i][2]
            carta_mano = self.mano[i]
            if carta_mano.valor == valor and carta_mano.pinta == pinta and carta_mano.color == color:
                self.bajas.append(carta_mano)
                return carta_mano
            else:
                raise NoExisteEnMano()

    def tomar_carta(self):
        self.emit("Tomar Carta", self)

    def recibir_carta(self, carta):
        if not isinstance(carta, Carta):
            raise TypeError(
                "El parámetro carta debe ser una instancia de la clase Carta")
        self.mano.append(carta)

    def tiene_cartas(self):
        return len(self.mano) > 0
