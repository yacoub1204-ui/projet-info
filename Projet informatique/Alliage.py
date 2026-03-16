class Alliage:

    def __init__(self, mv : list, list_prix : list, list_pct : list):
        self._mv = mv
        self._list_prix = list_prix
        self._list_pct = list_pct

    def get_mv(self):
        for i in range(len(self._mv)):
            self._mv[i] = self._mv[i]*10**3

        return self._mv
    
    def get_list_prix(self):
        return self._list_prix
    
    def get_list_pct(self):
        return self._list_pct
    
    def prix_total(self):
        return self._mv[0]*self._list_prix[0]*self._list_pct[0] + self._mv[1]*self._list_prix[1]*self._list_pct[1] + self._mv[2]*self._list_prix[2]**self._list_pct[2]