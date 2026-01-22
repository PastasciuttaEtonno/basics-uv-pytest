from operazioni import sottrazione

def test_sottrazione_positivi():
    assert sottrazione(5, 3) == 2

def test_sottrazione_negativi():
    assert sottrazione(-5, -3) == -2

def test_sottrazione_misti():
    assert sottrazione(-2, 3) == -5

def test_sottrazione_float():
    assert sottrazione(5.5, 3.5) == 2.0

def test_sottrazione_float_misti():
    assert sottrazione(-2.5, 3.5) == -6.0

def test_sottrazione_zero():
    assert sottrazione(0, 0) == 0

def test_sottrazione_con_stringa():
    assert sottrazione("hello", 3) is None

def test_sottrazione_con_none():
    assert sottrazione(None, 3) is None

def test_sottrazione_con_lista():
    assert sottrazione([1], 3) is None

def test_sottrazione_con_booleani():
    # In Python True = 1 e False = 0
    assert sottrazione(True, False) == 1