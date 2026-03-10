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

