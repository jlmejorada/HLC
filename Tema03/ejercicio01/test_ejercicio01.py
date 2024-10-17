from Ejercicio01 import cifraTexto

def test_cifra1():
    assert cifraTexto("h",3) == "k"

def test_cifra2():
    assert cifraTexto("hola",3) == "krñd"

