from operazioni import somma

def test_somma_positivi():
    assert somma(2, 3) == 5

def test_somma_negativi():
    assert somma(-2, -3) == -5

def test_somma_misti():
    assert somma(-2, 3) == 1

def test_somma_float():
    assert somma(2.5, 3.5) == 6.0

def test_somma_float_misti():
    assert somma(-2.5, 3.5) == 1.0

def test_somma_zero():
    assert somma(0, 0) == 0

def test_somma_con_stringa():
    assert somma("hello", 3) is None

def test_somma_con_none():
    assert somma(None, 3) is None

def test_somma_con_lista():
    assert somma([1], 3) is None

def test_somma_con_booleani():
    assert somma(True, False) == 1
