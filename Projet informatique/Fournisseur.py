class Fournisseur:
    def __init__(self, x, y, prix_unitaire):
        self._x = x
        self._y = y
        self._pu = prix_unitaire

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_pu(self):
        return self._pu