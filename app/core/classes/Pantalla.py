from os import system, name
from core.classes.Carta import Carta, str_a_carta, str_a_cartas
from core.classes.Ronda import Ronda


class Pantalla:
    def __init__(self) -> None:
        pass

    def borrar(self):
        name == 'nt' and system('cls') or system('clear')

    def mensaje_repartiendo_cartas(self):
        print("Repartiendo cartas...")

    def mensaje_personalizado(self, mensaje: str):
        print(mensaje)

    def mensaje_ganador(self, jugador):
        if jugador == None:
            print("No hay ganador")
        print(f"El ganador es {jugador.nombre} con {jugador.puntaje} puntos")

    def consulta_datos_jugador(self, i, parser=str):
        return parser(input(f"Ingrese el nombre del jugador {i+1}: "))

    def consultar_opcion(self, parser=str, *opciones_validas):
        option = parser(input("Ingrese una opcion: "))
        while (option not in opciones_validas):
            try:
                option = parser(input("Ingrese una opcion valida: "))
            except:
                option = parser(input("Ingrese una opcion valida: "))
        return option

    def consultar_seleccion_cartas(self):
        return str_a_cartas(input("Ingrese su seleccion de cartas (formato: valor1,pinta1,color1 valor2,pinta2,color2):\n"))

    def consultar_seleccion_carta(self):
        return str_a_carta(input("Ingrese su seleccion de cartas (formato: valor1,pinta1,color1:\n"))

    def info_partida(self, jugadores, ronda: Ronda, n_ronda: int):
        print(
            f"Informacion de la partida:\nNombre\tPuntaje")
        for jugador in jugadores:
            print(f"{jugador.nombre}\t{jugador.puntaje}")
        print(
            f"Objetivos de la ronda {n_ronda}:\nTrios: {ronda.trios}\nEscalas: {ronda.escalas}\n\n")

    def menu_turno(self, jugador):
        print(
            f"Turno de {jugador.nombre}\n1. Tomar carta\n2. Botar Carta\n3. Bajar Patron\n4. Descartar Carta\n5. Ver Mano\n6. Ver Baja\n7. Ver Mazo\n8. Ver Mazo de Descartes\n9. Ver Baja del contrincante\n")

    def menu_inicio(self):
        print("Menu de inicio\n1. Comenzar Partida\n2. Salir")

    def menu_botar_carta(self, jugador, contrincante):
        print(f"Baja de {jugador.nombre}:")
        self.mostrar_cartas(jugador.baja)
        print(f"Baja de {contrincante.nombre}:")
        self.mostrar_cartas(contrincante.baja)
        print(
            f"1. Botar en mi baja\n2. Botar en la baja de {contrincante.nombre}\n")

    def menu_bajar_patron(self):
        print("1. Bajar Trio\n2. Bajar Escala\n")

    def mostrar_cartas(self, cartas):
        if not isinstance(cartas, list):
            raise TypeError("El parámetro cartas debe ser una lista de cartas")
        for carta in cartas:
            if not isinstance(carta, Carta):
                raise TypeError(
                    "El parámetro cartas debe ser una lista de cartas")

        print("0. Volver\n\nvalor, pinta, color")
        for carta in cartas:
            print(carta)
