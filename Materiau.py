class Materiau:
    def __init__(self, mv, prix_kg):
        self._mv = mv
        self._prix_kg = prix_kg

    def get_mv(self):
        return self._mv
    
    def get_prix_kg(self):
        return self._prix_kg