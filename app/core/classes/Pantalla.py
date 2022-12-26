from os import system, name
from core.classes.Carta import Carta


class Pantalla:
    def __init__(self) -> None:
        pass

    def borrar(self):
        name == 'nt' and system('cls') or system('clear')

    def menu_inicio(self):
        print("Menu de inicio\n1. Comenzar Partida\n2. Salir")

    def mensaje_repartiendo_cartas(self):
        print("Repartiendo cartas...")

    def consulta_datos_jugador(self, i):
        print(f"Ingrese el nombre del jugador {i}: ")

    def consultar_seleccion(self):
        return "Ingrese su seleccion: "

    def consultar_seleccion_cartas(self):
        return "Ingrese su seleccion de cartas (formato: valor1,pinta1,color1 valor2,pinta2,color2):\n"

    def menu_partida(self, jugadores):
        nombres = ', '.join(map(lambda j: j.nombre, jugadores))

        print(
            f"Jugadores: {nombres}\n7.Ver Mazo\n8.Ver Mazo de Descartes\n9. Ver Baja Contrincante")

    def menu_turno(self, jugador):
        print(
            f"Turno de {jugador.nombre}\n1. Tomar carta\n2. Botar Carta\n3. Bajar Patron\n4. Descartar Carta\n5. Ver Mano 6. Ver Baja")

    def mostrar_cartas(self, cartas):
        if not isinstance(cartas, list):
            raise TypeError("El parámetro cartas debe ser una lista de cartas")
        for carta in cartas:
            if not isinstance(carta, Carta):
                raise TypeError(
                    "El parámetro cartas debe ser una lista de cartas")
        print("valor, pinta, color")
        for carta in cartas:
            print(f"{carta.valor}, {carta.pinta}, {carta.color}")
