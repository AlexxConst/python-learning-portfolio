import pytest
from calculator import calculate


def test_add():
    assert calculate(2, "+", 3) == 5


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(1, "/", 0)


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(1, "?", 2)


def test_minus():
    assert calculate(5, "-", 3) == 2
