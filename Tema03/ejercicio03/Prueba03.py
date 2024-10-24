from Ejercicio03 import comprobarCodigo

def test_corto():
    assert comprobarCodigo("658") == True

def test_EAN8():
    assert comprobarCodigo("65839522") == True

def test_EAN13():
    assert comprobarCodigo("8414533043847") == True

def test_largo():
    assert comprobarCodigo("841453304384756465") == False

def test_EAN8MenosNum():
    assert comprobarCodigo("65839522") == True