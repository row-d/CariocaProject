from app.core.classes.Mazo import Mazo
from app.core.classes.MazoDescarte import MazoDescarte
from app.core.classes.Jugador import Jugador


class Partida:
    def __init__(self, mazo, descarte, jugadores) -> None:
        if not isinstance(mazo, Mazo):
            raise TypeError(
                "El parámetro mazo debe ser una instancia de la clase Mazo")
        if not isinstance(descarte, MazoDescarte):
            raise TypeError(
                "El parámetro descarte debe ser una instancia de la clase MazoDescarte")
        if not isinstance(jugadores, list):
            raise TypeError(
                "El parámetro jugadores debe ser una lista de instancias de la clase Jugador")
        for jugador in jugadores:
            if not isinstance(jugador, Jugador):
                raise TypeError(
                    "El parámetro jugadores debe ser una lista de instancias de la clase Jugador")
        self.mazo = mazo
        self.descarte = descarte
        self.jugadores = jugadores
        self.rondas = []

    def agregar_ronda(self, ronda):
        self.rondas.append(ronda)
