from parchis.Recursos import *

def test_avanza_Posiciones_j1_d1_d1():
    Recursos.dado1 = 1
    Recursos.dado2 = 1
    res = 2
    miJuego = Recursos("Carmen", "Pedro")
    miJuego.fichaj1=0
    miJuego.fichaj2=0
    miJuego.avanza_Posiciones(1)
    assert miJuego.fichaj1 == res

def test_avanza_Posiciones_j2_d1_d1():
    Recursos.dado1 = 1
    Recursos.dado2 = 1
    res = 2
    miJuego = Recursos("Carmen", "Pedro")
    miJuego.fichaj1=0
    miJuego.fichaj2=0
    miJuego.avanza_Posiciones(2)
    assert miJuego.fichaj2 == res

def test_avanza_Posiciones_j1_rebota():
    Recursos.dado1 = 5
    Recursos.dado2 = 5
    res = 14
    miJuego = Recursos("Carmen", "Pedro")
    miJuego.fichaj1=16
    miJuego.fichaj2=0
    miJuego.avanza_Posiciones(1)
    assert miJuego.fichaj1 == res

def test_avanza_Posiciones_j2_rebota():
    Recursos.dado1 = 5
    Recursos.dado2 = 5
    res = 14
    miJuego = Recursos("Carmen", "Pedro")
    miJuego.fichaj1=0
    miJuego.fichaj2=16
    miJuego.avanza_Posiciones(2)
    assert miJuego.fichaj2 == res