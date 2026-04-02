import Polygone

class Figure:

    def __init__(self, nom, x, y, list_poly : list[Polygone], r=0) :
        self._nom = nom
        self._x = x
        self._y = y
        self._list_poly = list_poly
        self._r = r

    def get_nom(self):
        return self._nom

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y
    
    def get_list_poly(self):
        return self._list_poly
    
    def get_r(self):
        return self._r
    
    def set_r(self, r):
        self._r = r

    def __str__(self) -> str:
        return f"{self._nom}"
    
    def surface(self):
        return self._x * self._y
    
    def tourner(self) -> None :
        for poly in self._list_poly :
            for point in poly.get_points() :
                x1 = point.get_x() - self._x
                y1 = point.get_y() - self._y

                point.set_x(-y1 + self._x)
                point.set_y(x1 + self._y)
        
        x = self._x
        y = self._y

        self.set_x(y)
        self.set_y(x)
        self.set_r((self._r +1)%2)