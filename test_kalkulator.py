from kalkulator import osszeadas

def test_osszeadas():
    assert osszeadas(2, 3) == 5
    assert osszeadas(-1, 1) == 0
    assert osszeadas(10, 10) == 20
