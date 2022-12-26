from typing import List
from functools import reduce
from core.lib.event import EventEmitter
from core.classes.Ronda import Ronda
from core.classes.Carta import Carta, Cartas, Baja, str_a_carta, str_a_cartas


class PatronInvalido(Exception):
    def __init__(self):
        super().__init__("No se puede bajar el patron puesto que no cumple con las reglas de la ronda")


class NoExisteEnMano(Exception):
    def __init__(self, carta):
        super().__init__(
            f"La carta: {carta} no esta en la mano")


class RecepcionManoInvalida(TypeError):
    def __init__(self):
        super().__init__("No se puede recibir la mano ya que no se tiene cartas (Input vacio). ")


class Jugador(EventEmitter):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.puntaje = 0
        self.baja: Baja = []
        self._mano: Cartas = []

    def descartar_carta(self, carta):
        self.emit("descartar", carta)
        self._mano.remove(carta)

    def recibir_mano(self, mano):
        if not isinstance(mano, list):
            raise RecepcionManoInvalida()
        for carta in mano:
            if not isinstance(carta, Carta):
                raise RecepcionManoInvalida()
        if len(mano) > 0:
            self._mano = mano

    def bajar_patron(self, patron: Cartas, tipo: str):
        es_trio = Ronda.es_trio(patron)
        es_escala = Ronda.es_escala(patron)
        if not isinstance(tipo, str):
            raise TypeError("El parámetro tipo debe ser una cadena de texto")
        if tipo not in ["trio", "escala"]:
            raise ValueError("El parámetro tipo debe ser 'trio' o 'escala'")
        if tipo == "trio" and es_trio:
            self.baja.append(patron)
            self.puntaje = self.puntaje + \
                reduce(lambda x, y: x + y.valor.value, patron, 0)
            self._mano = [carta for carta in self._mano if carta not in patron]
        elif tipo == "escala" and es_escala:
            self.baja.append(patron)
            self.puntaje = self.puntaje + \
                reduce(lambda x, y: x + y.valor.value, patron, 0)
            self._mano = [carta for carta in self._mano if carta not in patron]

    def botar_carta(self, carta: str, contrincante=None):
        if carta not in self._mano:
            raise NoExisteEnMano()
        if isinstance(contrincante, Jugador):
            contrincante.trios.append(carta)
        else:
            self.tr
        self._mano.remove(carta)

    def tomar_carta(self):
        self.emit("Tomar Carta", self)

    def recibir_carta(self, carta):
        if not isinstance(carta, Carta):
            raise TypeError(
                "El parámetro carta debe ser una instancia de la clase Carta")
        self._mano.append(carta)

    def tiene_cartas(self):
        return len(self._mano) > 0


Jugadores = List[Jugador]
