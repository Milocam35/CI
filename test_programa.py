from funciones import esPrimo

def test_es_primo():
    assert esPrimo(5) is True
    assert esPrimo(6) is False
    assert esPrimo(8) is False
    assert esPrimo(3) is True