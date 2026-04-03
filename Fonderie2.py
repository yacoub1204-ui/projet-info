import Alliage2
import Tole
import Client
import Materiau

class Fonderie2:
    
    def __init__ (self, tole : list[Tole], list_mat : list[Materiau], list_all : list[Alliage2], client : Client, cout):
        self._tole = tole
        self._client = client
        self._list_mat = list_mat
        self._list_all = list_all
        self._cout = cout

    def get_tole(self):
        '''tole produite'''
        return self._tole
    
    def get_client(self):
        return self._client

    def get_cout(self):
        '''cout engendré par la fonte du métal et le laminage (€/cm^3)'''
        return self._cout
    
    def get_list_mat(self):
        '''liste des materiaux disponibles'''
        return self._list_mat
    
    def get_list_all(self):
        '''liste des alliages en stock à la fonderie'''
        return self._list_all
    
    def mv_alliage(self, j : int):
        mv = 0
        for i in range(len(self._list_mat)):
            mv += self._list_mat[i].get_mv() * self._list_all[j].get_list_pct()[i]
        return mv