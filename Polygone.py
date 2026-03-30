import Point

class Polygone:
    def __init__(self, points : list[Point]):
        self._points = points

    def get_points(self):
        return self._points
    
