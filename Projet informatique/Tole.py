import Alliage

class Tole:

    def __init__(self, x, y, z, all : Alliage):
        self._x = x
        self._y = y
        self._z = z
        self._all = all

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_z(self):
        return self._z

    def get_all(self):
        return self._all