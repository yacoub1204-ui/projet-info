from math import sqrt

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def distance(self, autre_p : Point):
        return sqrt((-self._x + autre_p.get_x)**2 + (-self._y + autre_p.get_y)**2)
    
    def distance_point_droite(self, A : Point, B : Point): 
        return abs((B.get_x() - A.get_x()) * (A.get_y() - self._y) - (A.get_x() - self._x) * (B.get_y() - A.get_x())) / A.distance(B)