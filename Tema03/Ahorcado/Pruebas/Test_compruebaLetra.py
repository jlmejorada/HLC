from Programa.Ahorcado import *

def test_comprueba_Letra_E():
    letra = 'E'
    res = "_E_____"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.compruebaLetra(letra)
    assert res == miJuego.palabraPista

def test_comprueba_Letra_e():
    letra = 'e'
    res = "_E_____"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.compruebaLetra(letra)
    assert res == miJuego.palabraPista

def test_comprueba_Letra_otra():
    letra = 'f'
    res = "f"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.compruebaLetra(letra)
    assert res == miJuego.noAcertadas

def test_comprueba_Letra_otra_otra():
    letra = 'f'
    res = "f g"
    miJuego = Ahorcado()
    miJuego.palabraSecreta="PERSONA"
    miJuego.compruebaLetra(letra)
    letra = 'g'
    miJuego.compruebaLetra(letra)
    assert res == miJuego.noAcertadas