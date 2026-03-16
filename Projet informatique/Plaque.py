import polygone

class Plaque:

    def __init__(self, x : float, y : float, fig : Polygone):
        self._x = x
        self._y = y
        self._fig = fig

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_fig(self):
        return self._fig


"""
def rotation(self,x,y):   A TERMINER
    

nouveau_min_x=min_x
nouveau_max_x=nouveau_min_x + (max_y-min_y)


nouveau_min_y=min_y
nouveau_max_y=nouveau_min_y +(max_x-min_x)
"""
