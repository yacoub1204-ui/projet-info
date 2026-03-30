import Point

class Polygone:
    def __init__(self, points : list[Point]):
        self._points = points

    def get_points(self):
        return self._points
        
      def point_plus_proche_droite(self, A, B):
        point_le_plus_proche = self._points[0]        
        distance_minimale = distance_point_droite(A, B, self._points[0])
        
        for point in self._points[1:]:                 
            d = distance_point_droite(A, B, point)
            if d < distance_minimale:
                distance_minimale = d
                point_le_plus_proche = point
        return point_le_plus_proche
