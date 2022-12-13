"""Build out tests for funcLog/*.py"""

from funcLog.mathcode import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(1, 2) == -1


def test_multiply():
    assert multiply(1, 2) == 2


def test_divide():
    assert divide(1, 2) == 0.5
