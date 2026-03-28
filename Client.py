class Client:

    def __init__(self, list_max : list, list_min : list):
        self._list_max = list_max
        self._list_min = list_min
    
    def get_list_max(self):
        '''pourcentages max de chaque matériau'''
        return self._list_max
    
    def get_list_min(self):
        '''pourcentages min de chaque matériau'''
        return self._list_min

    def composition_valide(self, list_pct: list):
        """True si tous les pourcentages sont dans les bornes min max"""
        for i in range(len(list_pct)):
            if list_pct[i] < self._list_min[i] or list_pct[i] > self._list_max[i]:
                return False
        return True
