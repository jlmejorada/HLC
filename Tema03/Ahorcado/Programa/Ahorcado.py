from random import randint


class Ahorcado:

    PALABRAS = ["HUMANIDAD", "PERSONA", "HOMBRE", "MUJER", "INDIVIDUO", "CUERPO", "PIERNA", "CABEZA", "BRAZO", "FAMILIA"]

    NUMINTENTOS = 7

    def __init__(self):
        self.palabraSecreta = ""
        self.palabraPista = ""
        self.noAcertadas = ""

    def generaPalabra(self):
        pos = randint(0, 9)
        self.palabraSecreta=Ahorcado.PALABRAS[pos]

    def compruebaLetra(self, letra):
        letraMayus=letra.upper()
        if letraMayus in self.palabraSecreta:
            for i in range(0,len(self.palabraSecreta)):
                if letraMayus == self.palabraSecreta[i]:
                    self.palabraPista += letraMayus
                else:
                    self.palabraPista += "_"
        else:
            if self.noAcertadas != "":
                self.noAcertadas += " "
            self.noAcertadas += letra

    def compruebaPalabra(self, palabra):
        palabraMayus=palabra.upper()
        # if palabra != self.palabraSecreta:
        #     pass
        if palabraMayus == self.palabraSecreta:
            self.palabraPista = palabraMayus

