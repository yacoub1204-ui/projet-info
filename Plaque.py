import Polygone

class Plaque:

    def __init__(self, x: float, y: float, dict_p: dict[Polygone], prix_d: float):
        self._x=x
        self.y=y
        self._prix_d = prix_d """euro/cm^2"""
        self._dict_p = dict_p


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_prix_d(self):
        return self._prix_d
    
    def get_dict_p(self):
        return self._dict_p

    def surface(self):
        return self._x*self._y


    def rotation(self):
        rotation_plaque=0
        return Plaque(self._y,self._x,self._dict_p,self._prix_d) rotation_plaque=1



    def rentre_dedans(self, tole_x,tole_y):
    """renvoie booléen"""
        return self.x<=tole_x and self._y <= tole_y


    def cout_decoupe(self):
        return self._prix_d*self.surface()
