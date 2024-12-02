from parchis.Recursos import *

def test_estado_carrera_j1():
    nombrej1 = "Carmen"
    nombrej2 = "Pedro"
    resEsp = nombrej1 + " va ganando la carrera"
    resRec = ""
    miJuego = Recursos(nombrej1, nombrej2)
    miJuego.fichaj1=8
    miJuego.fichaj2=4
    resRec = miJuego.estado_Carrera()
    assert resRec == resEsp

def test_estado_carrera_j2():
    nombrej1 = "Carmen"
    nombrej2 = "Pedro"
    resEsp = nombrej2 + " va ganando la carrera"
    resRec = ""
    miJuego = Recursos(nombrej1, nombrej2)
    miJuego.fichaj1=4
    miJuego.fichaj2=8
    resRec = miJuego.estado_Carrera()
    assert resRec == resEsp

def test_estado_carrera_empt():
    nombrej1 = "Carmen"
    nombrej2 = "Pedro"
    resEsp = "La carrera va empatada"
    resRec = ""
    miJuego = Recursos(nombrej1, nombrej2)
    miJuego.fichaj1=4
    miJuego.fichaj2=4
    resRec = miJuego.estado_Carrera()
    assert resRec == resEsp