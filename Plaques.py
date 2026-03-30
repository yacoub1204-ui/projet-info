import Polygone

class Plaques:

    def __init__(self, prix_d : float, dict_f : dict[Figures]):
        self._prix_d = prix_d
        self._dict_f = dict_f

    def get_prix_d(self):
        """renvoie le prix du déplacement du laser"""
        return self._prix_d
    
    def get_dict_f(self):
        """renvoie le dictionnaire contenant toutes les figures à découper dans chaque plaque"""
        return self._dict_f
    
    def get_list_f(self):
        """renvoie la liste de toutes les figures à découper dans chaque plaque"""
        list_f = []
        for cle in self.get_dict_f :
            list_f.append(cle)
        return list_f


