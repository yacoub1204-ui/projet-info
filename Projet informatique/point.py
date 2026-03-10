from math import sqrt

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def distance(autre_p : Point):
        return sqrt((-self._x + get_x(autre_p))**2 + (-self._y + get_y(autre_p))**2)