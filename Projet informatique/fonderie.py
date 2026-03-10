import materiau
import taule

class Fonderie:
    
    def __init__ (self, x : float, y : float, client : Client, cout : float, list_mat : list[Materiau], ):
        self._x = x
        self._y = y
        self._client = client
        self._cout = cout
        self._list_mat = list_mat

    def get_x(self):
        '''longeur des toles produites (cm)'''
        return self._x
    
    def get_y(self):
        '''largeur des toles produites (cm)'''
        return self._y
    
    def get_z(self):
        '''épaisseur demandée par le client (cm)'''
        return self._z
    
    def get_cout(self):
        '''cout engendré par la fonte du métal et le laminage (€/cm^3)'''
        return self._cout
    
    def get_list_mat(self):
        return self._list_mat



