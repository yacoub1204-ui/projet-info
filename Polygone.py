from __future__ import annotations  # CORRIGE : forward reference pour Point
import Point

class Polygone:
    def __init__(self, points : list[Point.Point]):
        self._points = points

    def get_points(self):
        return self._points

    def get_list_points(self):      
        return self._points

    def point_plus_proche_droite(self, A, B):
        point_le_plus_proche = self._points[0]
        distance_minimale = self._points[0].distance_point_droite(A, B)

        for point in self._points[1:]:
            d = point.distance_point_droite(A, B)
            if d < distance_minimale:
                distance_minimale = d
                point_le_plus_proche = point
        return point_le_plus_proche
