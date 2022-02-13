from math import hypot


class Vector:
    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = float(value)

    @y.setter
    def y(self, value):
        self._y = float(value)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def vector_len(self):
        return hypot(self.x, self.y)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
        
    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        return self

    def __iadd__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other


if __name__ == '__main__':  # pragma: no cover
    a = Vector(2, 8)
    b = Vector(3, 4)

    if a == b:
        print(f'{a} == {b}')
    else:
        print(f'{a} != {b}')

    print(a, id(a))
    print(b, id(b))
    a += b
    print(f'Vector a + b = {a}, id:{id(a)}')
    print('Vector length = ', a.vector_len())
    a -= b
    print(f'Vector a - b = {a}, id:{id(a)}')
    print('Vector length = ', a.vector_len())

    c = a - b
    print(c, id(c))

    print(a, id(a))
    print(b, id(b))
