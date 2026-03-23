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
        prix_kg=0
        for i in range(len(self._list_prix)):
            prix_kg+=self._list_prix[i]*self._list_pct[i]  
        return prix_kg
        
        
    def prix_m3(self):
        mv = self.convert_mv()
        prix_m3=0
        for i in range(len(self._list_prix)):
            prix_m3+=self._list_prix[i]*self._list_pct[i]*mv[i]
        return prix_m3
    
    def prix_cm3(self):
        return self.prix_m3()*10**6
