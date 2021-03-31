import FactorialFinder


def test_fact():
    assert FactorialFinder.findFactRecursive(5) == 120
    assert FactorialFinder.findFactRecursive(4) == 24
