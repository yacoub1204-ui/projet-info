class Tole:

    def __init__(self, x, y, z, mat):
        self._x = x
        self._y = y
        self._z = z
        self._mat = mat
        self._plaques = []  # plaques deja decoupees
        self._zone_dispo = [(0, 0, x, y)]  # espace tole dispo
    def ajouter_plaque(self, plaque):
        self._plaques.append(plaque)


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_z(self):
        return self._z

    def get_mat(self):
        return self._mat


    def decouper_plaque(self, plaque):
        if plaque._x<= self._zones_libres[2] and plaque._y <= self._zones_libres[3] :        
            plaque._x= x
            plaque._y=y
            self._plaques.append(plaque)
           
