import Polygone

class Figure:

    def __init__(self, x, y, list_p : list[Polygone]) :
        self._x = x
        self._y = y
        self._list_p = list_p

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_list_p(self):
        return self._list_p
    
    def surface(self):
        return self._x * self._y
    
    def tourner(self) -> None :
        for poly in self._list_p :
            for point in poly.get_points() :
                point.get_x() - self._x ; point.get_y() - self._y = point.get_y() - self._y ; point.get_x() - self._x
        self._x ; self._y = self._y ; self._x
    
    def decoupe_fig_tr(self):
        solution=[]
        for element in self._list_f() :
            solution.append(element[0])
        return solution

    def point_plus_loin(self):
        point_max = None
        distance_max = 0
    
        origine = Point(0, 0)
    
        for polygone in self._list_p :
            for point in polygone.get_points():
                d = point.distance( origine)
                if d > distance_max:
                    distance_max = d
                    point_max = point
                
        return point_max
