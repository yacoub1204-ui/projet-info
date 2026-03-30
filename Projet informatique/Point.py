from math import sqrt

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    def set_x(self, x):
        self._x=x
    def set_y(self, y):
        self._y=y

    def distance(self, autre_p : Point):
        return sqrt((-self._x + autre_p.get_x())**2 + (-self._y + autre_p.get_y())**2)
