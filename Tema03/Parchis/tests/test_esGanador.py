from parchis.Recursos import *

def test_es_Ganador_j1():
    nombrej1 = "Carmen"
    nombrej2 = "Pedro"
    resEsp = nombrej1
    resRec = ""
    miJuego = Recursos(nombrej1, nombrej2)
    miJuego.fichaj1 = Recursos.TAM_TABLERO
    miJuego.fichaj2 = 8
    resRec = miJuego.es_Ganador()
    assert resRec == resEsp

def test_es_Ganador_j2():
    nombrej1 = "Carmen"
    nombrej2 = "Pedro"
    resEsp = nombrej2
    resRec = ""
    miJuego = Recursos(nombrej1, nombrej2)
    miJuego.fichaj1 = 8
    miJuego.fichaj2 = Recursos.TAM_TABLERO
    resRec = miJuego.es_Ganador()
    assert resRec == resEsp

def test_es_Ganador_none():
    nombrej1 = "Carmen"
    nombrej2 = "Pedro"
    resEsp = ""
    resRec = ""
    miJuego = Recursos(nombrej1, nombrej2)
    miJuego.fichaj1 = 14
    miJuego.fichaj2 = 8
    resRec = miJuego.es_Ganador()
    assert resRec == resEsp