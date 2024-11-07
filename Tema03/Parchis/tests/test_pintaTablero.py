from parchis.Recursos import *

def test_pinta_tablero():
    nombre1="Juana"
    nombre2="Pedro"
    linea=""
    miJuego = Recursos(nombre1,nombre2)
    comprueba = miJuego.pinta_tablero(miJuego)
    linea+= "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    linea+= str(nombre1) + "\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    linea += str(nombre2) + "\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    assert linea == comprueba


def test_pinta_tablero_ficha4():
    nombre1 = "Juana"
    nombre2 = "Pedro"
    linea = ""
    miJuego = Recursos(nombre1, nombre2)
    miJuego.fichaj1 = 4
    miJuego.fichaj2 = 4
    comprueba = miJuego.pinta_tablero(miJuego)
    linea += "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    linea += str(nombre1) + "\tI\t\t\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    linea += str(nombre2) + "\tI\t\t\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    assert linea == comprueba

def test_pinta_tablero_fichaA4_fichaB12():
    nombre1 = "Juana"
    nombre2 = "Pedro"
    linea = ""
    miJuego = Recursos(nombre1, nombre2)
    miJuego.fichaj1 = 4
    miJuego.fichaj2 = 12
    comprueba = miJuego.pinta_tablero(miJuego)
    linea += "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    linea += str(nombre1) + "\tI\t\t\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    linea += str(nombre2) + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\tO\t\t\t\t\t\t\tF"
    assert linea == comprueba

def test_pinta_tablero_fichaA0_fichaB14():
    nombre1 = "Juana"
    nombre2 = "Pedro"
    linea = ""
    miJuego = Recursos(nombre1, nombre2)
    miJuego.fichaj2 = 14
    comprueba = miJuego.pinta_tablero(miJuego)
    linea += "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    linea += str(nombre1) + "\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    linea += str(nombre2) + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tO\t\t\t\t\tF"
    assert linea == comprueba