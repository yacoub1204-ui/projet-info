from __future__ import annotations
import Alliage2
import Tole
import Client
import Materiau

class Fonderie2:

    def __init__(self, tole : Tole.Tole, liste_mat : list, list_all : list, client : Client.Client, cout):
        self._tole     = [tole]     # CORRIGE : wrappé en liste car get_tole()[0] utilisé partout
        self._client   = client
        self._liste_mat = liste_mat
        self._list_all = list_all
        self._cout     = cout

    def get_tole(self):
        '''liste des toles produites'''
        return self._tole

    def get_cout(self):
        '''cout engendré par la fonte du métal et le laminage (€/cm^3)'''
        return self._cout

    def get_liste_mat(self):
        '''liste des materiaux disponibles'''
        return self._liste_mat

    def get_list_all(self):
        '''liste des alliages en stock à la fonderie'''
        return self._list_all

    def get_client(self):           # CORRIGE : manquait, utilisé dans solutions_fournisseurs
        return self._client
