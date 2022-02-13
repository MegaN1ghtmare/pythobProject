import pytest
from math import hypot

from vector.vector import Vector


def test_constructor():
    a = Vector()
    b = Vector(5, 5)

    assert a.x == 0.0
    assert a.y == 0.0
    assert b.x == 5.0
    assert b.y == 5.0


def test_constructor_exceptions():
    with pytest.raises(ValueError):
        Vector('WTF', 'OMG')

    with pytest.raises(TypeError):
        Vector(Vector(), Vector())


def test_setters():
    a = Vector()

    assert a.x == 0.0
    assert a.y == 0.0

    a.x = -9
    a.y = 42

    assert a.x == -9.0
    assert a.y == 42.0


def test_setters_exceptions():
    a = Vector()

    with pytest.raises(ValueError):
        a.x = 'error'

    with pytest.raises(TypeError):
        a.y = Vector()


def test_str_representation():
    out = str(Vector())
    assert out == 'Vector(0.0, 0.0)'


def test_vector_len():
    b = Vector(2, 2)

    assert b.vector_len() == hypot(2, 2)


def test_vector_increment():
    a = Vector()
    b = Vector(4, 5)
    a += b

    assert a.x == 4.0
    assert a.y == 5.0


def test_vector_decrement():
    a = Vector()
    b = Vector(-9, 5)
    a -= b

    assert a.x == 9.0
    assert a.y == -5.0


def test_vector_addition():
    a = Vector(1, 1)
    b = Vector(10, 10)
    c = a + b

    assert c.x == 11.0
    assert c.y == 11.0


def test_vector_subtraction():
    a = Vector(10, 10)
    b = Vector(1, 1)
    c = a - b

    assert c.x == 9.0
    assert c.y == 9.0


def test_operators():
    a = Vector()
    b = Vector(1, 2)

    assert a != b
    assert not a == b
