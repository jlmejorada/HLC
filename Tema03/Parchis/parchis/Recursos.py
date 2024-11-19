from random import randint


class Recursos:

    # Atributo constante estatico
    TAM_TABLERO = 20
    # Atributos estaticos
    dado1 = 0
    dado2 = 0

    # Definimos en el constructor los atributos no estaticos
    def __init__(self, nombrej1, nombrej2):
        self.fichaj1 = 0
        self.fichaj2 = 0
        self.nombrej1 = nombrej1
        self.nombrej2 = nombrej2

    # Es un metodo estatico que tira dos dados con numeros entre 1 y 6
    @staticmethod
    def tira_dados():
        Recursos.dado1 = randint(1,6)
        Recursos.dado2 = randint(1, 6)

    # Pinta un tablero con la posicion de las fichas de los jugadores
    def pinta_tablero(self):
        linea=""
        i = 0
        while i <= Recursos.TAM_TABLERO:
            if i == 0:
                linea += "\t\t" + "I"
            elif i == Recursos.TAM_TABLERO:
                linea+="\t" + "F\n"
            else:
                linea+="\t" + str(i)
            i += 1

        i = 0
        linea+=self.nombrej1 + "\tI"
        while i <= Recursos.TAM_TABLERO:
            linea += "\t"
            if i == self.fichaj1 :
               linea+="O"
               i += 1
            elif i == Recursos.TAM_TABLERO:
                linea += "F\n"
            i += 1

        i = 0
        linea += self.nombrej2 + "\tI"
        while i <= Recursos.TAM_TABLERO:
            linea += "\t"
            if i == self.fichaj2:
                linea += "O"
                i += 1
            elif i == Recursos.TAM_TABLERO:
                linea += "F"
            i += 1

        # region CODIGOANTIGUO
        # for i in range(1,4):
        #     if i == 2:
        #         linea += self.nombrej1
        #     elif i == 3:
        #         linea += self.nombrej2
        #     linea += "\tI"
        #
        # for j in range(1,Recursos.TAM_TABLERO):
        #     linea += "\t"
        #     if i == 1:
        #         linea += str(j)
        #     elif i == 2:
        #         if j == self.fichaj1:
        #             linea += "O"
        #     elif i == 3:
        #         if j == self.fichaj2:
        #             linea += "O"
        # linea += "\tF\n"
        # endregion
        return linea

    # Avanza la posicion de los jugadores según el turno
    def avanza_Posiciones(self, turno):
        if (turno == 1):
            self.fichaj1 += Recursos.dado1 + Recursos.dado2
            if (self.fichaj1 > Recursos.TAM_TABLERO):
                self.fichaj1 = Recursos.TAM_TABLERO - (self.fichaj1 - Recursos.TAM_TABLERO)
        elif (turno == 2):
            self.fichaj2 += Recursos.dado1 + Recursos.dado2
            if (self.fichaj2 > Recursos.TAM_TABLERO):
                self.fichaj2 = Recursos.TAM_TABLERO - (self.fichaj2 - Recursos.TAM_TABLERO)

    # Si un jugador va por delante de otro, manda un mensaje diciendolo, si no, dice el empate
    def estado_Carrera(self):
        res = ""
        if (self.fichaj1 > self.fichaj2):
            res = self.nombrej1 + " va ganando la carrera"
        elif (self.fichaj1 < self.fichaj2):
            res = self.nombrej2 + " va ganando la carrera"
        else:
            res = "La carrera va empatada"
        return res

    # Si un jugador llega a la meta, se devuelve su nombre, si no, se devuelve cadena vacia
    def es_Ganador(self):
        res = ""
        if (self.fichaj1 == Recursos.TAM_TABLERO):
            res = self.nombrej1
        elif (self.fichaj2 == Recursos.TAM_TABLERO):
            res = self.nombrej2
        return res