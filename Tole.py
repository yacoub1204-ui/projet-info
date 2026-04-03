class Tole:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self._all = all

    def get_x(self):
        '''largeur de la taule en stock'''
        return self._x

    def get_y(self):
        '''hateur de la tole en stock'''
        return self._y
    
    def get_z(self):
        '''épaisseur de la tole en stock'''
        return self._z