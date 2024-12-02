from Programa.Ahorcado import *

def test_genera_Palabra():
    miJuego = Ahorcado()
    miJuego.generaPalabra()
    assert miJuego.palabraSecreta in Ahorcado.PALABRAS
