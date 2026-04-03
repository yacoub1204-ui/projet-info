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

    def get_pct_max(self):      # CORRIGE : alias utilisé dans solutions_fournisseurs
        return self._list_max

    def get_pct_min(self):      # CORRIGE : alias utilisé dans solutions_fournisseurs
        return self._list_min
