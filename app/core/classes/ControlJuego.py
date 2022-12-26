from random import shuffle

from core.enums.Color import Color
from core.enums.Pinta import Pinta
from core.enums.ValorDeCarta import ValorDeCarta

from core.classes.Carta import Carta
from core.classes.Pantalla import Pantalla
from core.classes.Jugador import Jugador
from core.classes.Mazo import Mazo
from core.classes.MazoDescarte import MazoDescarte
from core.classes.Partida import Partida
from core.classes.Ronda import Ronda


class ControlJuego:
    def __init__(self, pantalla) -> None:
        if not isinstance(pantalla, Pantalla):
            raise TypeError(
                "El parámetro pantalla debe ser una instancia de la clase Pantalla")
        self.pantalla = pantalla
        self.ronda = 1
        self.turno = 0

    def iniciar_juego(self):
        self.pantalla.menu_inicio()
        seleccion = input(self.pantalla.consultar_seleccion())
        while (seleccion != "1" and seleccion != "2"):
            if seleccion == "1":
                return self.iniciar_partida()
            elif seleccion == "2":
                exit(0)

    def crear_baraja_inglesa(self):
        baraja_inglesa = []
        for pinta in range(1, 5):
            for valor in range(1, 14):
                for color in range(30, 32):
                    baraja_inglesa.append(
                        Carta(color=Color(color), pinta=Pinta(pinta), valor=ValorDeCarta(valor)))
        return baraja_inglesa

    def iniciar_partida(self):
        jugadores = [None, None]
        cartas_por_jugador = 12
        baraja_inglesa = self.crear_baraja_inglesa()

        # se crean los mazos
        descarte = MazoDescarte()
        mazo = Mazo(baraja_inglesa)

        # se baraja el mazo
        mazo.desordenar()

        # se crean los jugadores
        for i in range(len(jugadores)):
            self.pantalla.consulta_datos_jugador(i)
            nombre = input()
            jugador = Jugador(nombre)
            jugadores[i] = jugador
            self.pantalla.borrar()

        # se reparten las cartas
        self.pantalla.mensaje_repartiendo_cartas()
        for jugador in jugadores:
            mano = []
            for i in range(cartas_por_jugador+1):
                mano.append((mazo.sacar_carta()))
            jugador.recibirMano(mano)

        # se crea la partida
        partida = Partida(mazo, descarte, jugadores)

        ronda1 = Ronda(2, 0)
        ronda2 = Ronda(1, 1)

        partida.agregar_ronda(ronda1)
        partida.agregar_ronda(ronda2)

        while (partida.rondas != 0):
            while (any(jugador.tiene_cartas() for jugador in partida.jugadores)):
                jugador = partida.jugadores[self.turno]
                jugador.on("Tomar Carta",
                           lambda jugador: jugador.recibir_carta(partida.mazo.sacar_carta()))
                self.pantalla.menu_partida(partida.jugadores)
                self.pantalla.menu_turno(jugador)
                self.pantalla.consultar_seleccion()

                seleccion = int(input())
                while (seleccion > 0 and seleccion < 10):
                    if seleccion == 1:
                        jugador.tomar_carta()

                    elif seleccion == 2:
                        self.pantalla.borrar()
                        self.pantalla.mostrar_cartas(jugador.mano)
                        self.pantalla.consultar_seleccion_cartas()
                        cartas = input()

                    if seleccion == 4:
                        self.turno = (self.turno + 1) % len(partida.jugadores)
                        continue
                    self.pantalla.borrar()

            partida.rondas.pop()
            self.pantalla.borrar()
