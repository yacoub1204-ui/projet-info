import Point

class Figure:
    def __init__(self, x, y, points : list[Point]):
        self._x = x
        self._y = y
        self._points = points

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def get_points(self):
        return self._points
