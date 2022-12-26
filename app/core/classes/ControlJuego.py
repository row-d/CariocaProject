from random import shuffle

from core.enums.Color import Color
from core.enums.Pinta import Pinta
from core.enums.ValorDeCarta import ValorDeCarta

from core.classes.Carta import Carta, Cartas
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
        self.ronda = 0
        self.turno = 0

    def iniciar_juego(self):
        self.pantalla.menu_inicio()
        seleccion = self.pantalla.consultar_opcion(int, 1, 2)
        if seleccion == 1:
            self.iniciar_partida()
        elif seleccion == 2:
            exit(0)

    def crear_baraja_inglesa(self) -> Cartas:
        baraja_inglesa = []
        for pinta in range(1, 5):
            for valor in range(2, 14):
                for color in range(30, 32):
                    baraja_inglesa.append(
                        Carta(color=Color(color), pinta=Pinta(
                            pinta), valor=ValorDeCarta(valor)))

        return baraja_inglesa

    def refrescar_pantalla(self, partida: Partida, jugador: Jugador):
        self.pantalla.borrar()
        self.pantalla.info_partida(
            partida.jugadores, partida.rondas[self.ronda], self.ronda+1)
        self.pantalla.menu_turno(jugador)

    def iniciar_partida(self):
        jugadores_total = 2
        cartas_por_jugador = 12
        _jugadores = [None for _ in range(jugadores_total)]
        baraja_inglesa = self.crear_baraja_inglesa()

        # se crean los mazos
        descarte = MazoDescarte()
        mazo = Mazo(baraja_inglesa)

        # se baraja el mazo
        mazo.desordenar()

        # se crean los jugadores
        for i in range(len(_jugadores)):
            self.pantalla.borrar()
            nombre = self.pantalla.consulta_datos_jugador(i)
            jugador = Jugador(nombre)
            _jugadores[i] = jugador

        # se reparten las cartas
        self.pantalla.mensaje_repartiendo_cartas()
        for jugador in _jugadores:
            mano: Cartas = []
            for _ in range(cartas_por_jugador + 1):
                mano.append(mazo.tomar_carta())
            jugador.recibir_mano(mano)

        # se crea la partida
        self.partida = Partida(mazo, descarte, _jugadores)

        rondas = (Ronda(2, 0), Ronda(1, 1))
        for ronda in rondas:
            self.partida.agregar_ronda(ronda)

        for _jugador in self.partida.jugadores:
            _jugador.on("Tomar Carta",
                        lambda j: j.recibir_carta(self.partida.mazo.tomar_carta()))

        while (self.partida.rondas != 0):
            while (any(jugador.tiene_cartas() for jugador in self.partida.jugadores)):
                jugador = self.partida.jugadores[self.turno]
                i_con = (self.turno + 1) % len(self.partida.jugadores)
                contrincante = self.partida.jugadores[i_con]

                self.refrescar_pantalla(self.partida, jugador)

                seleccion = self.pantalla.consultar_opcion(int, *range(1, 10))
                # tomar carta
                if seleccion == 1:
                    jugador.tomar_carta()
                # botar carta
                if seleccion == 2:
                    self.pantalla.borrar()
                    self.pantalla.mostrar_cartas(jugador._mano)
                    carta = self.pantalla.consultar_seleccion_carta()
                    self.pantalla.menu_botar_carta()
                    subseleccion = self.pantalla.consultar_opcion(
                        int, 1, 2)
                    if subseleccion == 1:
                        jugador.botar_carta(carta)
                    elif subseleccion == 2:
                        jugador.botar_carta(carta, contrincante)

                # bajar patron
                if seleccion == 3:
                    self.pantalla.borrar()
                    self.pantalla.mostrar_cartas(jugador._mano)
                    self.pantalla.menu_bajar_patron()
                    subseleccion = self.pantalla.consultar_opcion(
                        int, *range(0, 3))
                    if subseleccion == 0:
                        self.refrescar_pantalla(self.partida, jugador)
                    elif subseleccion == 1:
                        cartas = self.pantalla.consultar_seleccion_cartas()
                        jugador.bajar_patron(cartas, "trio")
                    elif subseleccion == 2:
                        cartas = self.pantalla.consultar_seleccion_cartas()
                        jugador.bajar_patron(cartas, "escala")
                # descartar carta
                if seleccion == 4:
                    jugador.descartar_carta()
                    self.turno = (self.turno + 1) % len(self.partida.jugadores)

                # ver mano
                if seleccion == 5:
                    self.pantalla.mostrar_cartas(jugador._mano)
                    subseleccion = self.pantalla.consultar_opcion(int,
                                                                  0)
                    if subseleccion == 0:
                        self.refrescar_pantalla(self.partida, jugador)
                # ver baja
                if seleccion == 6:
                    self.pantalla.mostrar_cartas(jugador.baja)
                    subseleccion = self.pantalla.consultar_opcion(int,
                                                                  0)
                    if subseleccion == 0:
                        self.refrescar_pantalla(self.partida, jugador)
                # ver mazo
                if seleccion == 7:
                    self.pantalla.mostrar_cartas(self.partida.mazo.cartas)
                    subseleccion = self.pantalla.consultar_opcion(int,
                                                                  0)
                    if subseleccion == 0:
                        self.refrescar_pantalla(self.partida, contrincante)
                # ver descarte
                if seleccion == 8:
                    self.pantalla.mostrar_cartas(self.partida.descarte.cartas)
                    subseleccion = self.pantalla.consultar_opcion(int,
                                                                  0)
                    if subseleccion == 0:
                        self.refrescar_pantalla(self.partida, contrincante)
                # ver baja contrincante
                if seleccion == 9:
                    self.pantalla.mostrar_cartas(contrincante.baja)
                    subseleccion = self.pantalla.consultar_opcion(int,
                                                                  0)
                    if subseleccion == 0:
                        self.refrescar_pantalla(self.partida, contrincante)
            # verificar bajas si cumplen con los requisitos de la ronda
            for __jugador in self.partida.jugadores:
                if self.partida.rondas[self.turno].verificar_patrones(__jugador.baja):
                    self.partida.rondas.pop(0)
                    self.pantalla.borrar()

        ganador = self.partida.obtener_ganador()
        self.pantalla.mensaje_ganador(ganador)
