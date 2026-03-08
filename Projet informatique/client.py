import materiau

class Client:

    def __init__(self, z : float, dict_quantites : dict[Materiau : [[float][float]]]):
        self._z = z
        self._dict_quantites = dict_quantites

    def get_z(self):
        '''épaisseur demandée par le client'''
        return self._z
    
    def get_dict_quantites(self):
        '''dictionnaire contenant les %ages min et max de matériau voulu par le client'''
        return self._dict_quantites
    
    def get_pmax(self, dict_quantites, mat : Materiau):
        return dict_quantites[mat][0]
    
    def get_pmax(self, dict_quantites, mat : Materiau):
        return dict_quantites[mat][1]
