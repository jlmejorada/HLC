from parchis.Recursos import *

def test_tira_dados():
    Recursos.tira_dados()
    assert 1 <= Recursos.dado1 <= 6
    assert 1 <=  Recursos.dado2 <= 6



