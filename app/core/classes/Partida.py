from core.classes.Mazo import Mazo
from core.classes.MazoDescarte import MazoDescarte
from core.classes.Jugador import Jugador, Jugadores


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
        self.jugadores: Jugadores = jugadores
        self.rondas = []

    def agregar_ronda(self, ronda):
        self.rondas.append(ronda)

    def obtener_ganador(self):
        puntajes = []
        for jugador in self.jugadores:
            puntajes.append(jugador.puntaje)
        # verifica si hubo empate
        if puntajes.count(max(puntajes)) > 1:
            return None
        return self.jugadores[puntajes.index(max(puntajes))]
