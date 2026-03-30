class Alliage:

    def __init__(self, mv : list, list_prix : list, list_pct : list):
        self._mv = mv
        self._list_prix = list_prix
        self._list_pct = list_pct

    def convert_mv(self):
        '''convertis les masses volumiques données en g/cm**3 en kg/m3'''
        lc = self._mv
        for i in range(len(lc)):
            lc[i] = lc[i]*10**3
        return lc
    
    def get_mv(self):
        return self._mv
    
    def get_list_prix(self):
        return self._list_prix
    
    def get_list_pct(self):
        return self._list_pct
    
    def prix_kg(self):
        return self._list_prix[0]*self._list_pct[0] + self._list_prix[1]*self._list_pct[1] + self._list_prix[2]*self._list_pct[2]
    
    def prix_m3(self):
        mv = self.convert_mv()
        return self._list_prix[0]*self._list_pct[0]*mv[0] + self._list_prix[1]*self._list_pct[1]*mv[1] + self._list_prix[2]*self._list_pct[2]*mv[2]
    
    def prix_cm3(self):
        return self.prix_m3()*10**6