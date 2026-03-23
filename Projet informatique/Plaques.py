import Polygone

class Plaque:

    def __init__(self, prix_d : float, dict_p : dict[Polygone]):
        self._prix_d = prix_d
        self._dict_p = dict_p

    def get_prix_d(self):
        return self._prix_d
    
    def get_dict_p(self):
        return self._dict_p

