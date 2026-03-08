class Materiau:

    def __init__(self, mv, prix):
        self._mv = mv
        self._prix = prix

    def get_mv(self):
        return self._mv
    
    def get_prix(self):
        return self._prix