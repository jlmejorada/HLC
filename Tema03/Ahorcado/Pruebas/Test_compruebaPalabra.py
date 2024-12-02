from Programa.Ahorcado import *

def test_comprueba_Palabra_PEDRO():
    palabra = "PEDRO"
    res = "PE_____"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.palabraPista = "PE_____"
    miJuego.compruebaPalabra(palabra)
    assert res == miJuego.palabraPista

def test_comprueba_Palabra_PERSONA():
    palabra = "PERSONA"
    res = "PERSONA"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.compruebaPalabra(palabra)
    assert res == miJuego.palabraPista

def test_comprueba_Palabra_persona():
    palabra = "persona"
    res = "PERSONA"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.compruebaPalabra(palabra)
    assert res == miJuego.palabraPista

def test_comprueba_Palabra_peRSoNa():
    palabra = "peRSoNa"
    res = "PERSONA"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.compruebaPalabra(palabra)
    assert res == miJuego.palabraPista