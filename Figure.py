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
    
    def decoupe_fig_tr(self):
        solution=[]
        for element in self._list_f() :
            solution.append(element[0])
        return solution