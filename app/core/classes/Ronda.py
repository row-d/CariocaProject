

class Ronda:
    def __init__(self, trios: int, escalas: int) -> None:
        if trios <= 0 and escalas <= 0:
            raise ValueError(
                "Los valores de trios y escalas deben ser mayores a 0")
        self.trios = trios
        self.escalas = escalas

    def verificar_patrones(self, patron1, patron2):
        patrones = [patron1, patron2]
        trios = 0
        escalas = 0
        for patron in patrones:
            if self.es_trio(patron):
                trios += 1
            if self.es_escala(patron):
                escalas += 1
        return trios == self.trios and escalas == self.escalas

    def es_trio(patron):
        if len(patron) != 3:
            return False
        for carta in patron:
            if carta.valor != patron[0].valor:
                return False
        return True

    def es_escala(patron: list):
        if len(patron) != 4:
            return False
        patron.sort(key=lambda carta: carta.valor)
        valor_actual = patron[0].valor
        for carta in range(1, len(patron)):
            if carta.valor != valor_actual + 1:
                return False
            valor_actual = carta.valor
            if carta.pinta != patron[0].pinta:
                return False
        return True


'''
        alicia ----> 2 trios
        verificar patrones
            esTrios()
            true -----> alicia.bajarPatron(patron)
                alicia.patron1 = patron

    
    alicia y pedro
    
    turno alicia:
        for jugador in jugadores:
            jugador.on("bajar",lambda patron: Juego.Ronda1.verificarPatron(patron))
        

        A A A  555   //// jugador 1

        4768 A //// jugador 2

        A A A A //// JUGADOR 1\
        
        4768 5 //// JUGADOR 2    
        A A A 5555 //// JUGADOR 1

        476   //// JUGADOR 2




        patron = alicia.bajarPatron(patron) 
        if patron != None:
            mesa.append(patron)
        else:
            print("No se puede bajar ese patron porque no es un trio/escala")
        
        def bajarPatron(patron: str):
            self.emit("bajar",patron)
            return patron
        2,3,4,5
        mesa = [ patron1[jugador1], patron2]
'''
