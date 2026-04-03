class Alliage2:
    def __init__(self, list_pct, kg):   # CORRIGE : ordre inversé pour correspondre à reader2 Alliage2(pct, poids)
        self._kg = kg
        self._list_pct = list_pct

    def get_kg(self):
        return self._kg

    def get_list_pct(self):             # CORRIGE : manquait, utilisé dans solutions_fournisseurs
        return self._list_pct

    def get_dict_alliage(self):
        return self._list_pct
