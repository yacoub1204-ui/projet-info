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
        return sqrt((-self._x + autre_p.get_x)**2 + (-self._y + autre_p.get_y)**2)
    
    def distance_point_droite(self, A : Point, B : Point): 
        return abs((B.get_x() - A.get_x()) * (A.get_y() - self._y) - (A.get_x() - self._x) * (B.get_y() - A.get_y())) / A.distance(B)
    def point_proche_liste(self, points):
        if not points:
            return None
        point_le_plus_proche = points[0]
        distance_minimale = self.distance(points[0])
        for point in points[1:]:
            dist = self.distance(point)
            if dist < distance_minimale:
                distance_minimale = dist
                point_le_plus_proche = point
    
        return point_le_plus_proche
                    
    def classementpoint(self,liste,concurent)  :
        clas=[]
        for _ in range(concurent):
            clas.append(self.point_proche_liste(liste))
            liste.remove(self.point_proche_liste(liste))
        return clas
