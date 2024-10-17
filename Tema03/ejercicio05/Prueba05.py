from Ejercicio05 import ascensor

def test_piso0():
    assert ascensor("0") == 0

def test_piso1():
    assert ascensor("1") == 1

def test_piso01():
    assert ascensor("0 1") == 1

def test_piso10():
    assert ascensor("1 0") == 1

def test_piso024():
    assert ascensor("0 2 4") == 4

def test_piso021():
    assert ascensor("0 2 1") == 3

def test_piso102():
    assert ascensor("1 0 2") == 3

def test_piso10287():
    assert ascensor("1 0 2 8 7") == 10

def test_piso80287():
    assert ascensor("8 0 2 8 7") == 17

def test_piso204287():
    assert ascensor("2 0 4 2 8 7") == 15







