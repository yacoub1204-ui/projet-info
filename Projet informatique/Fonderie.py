import materiau
import tole
import client

class Fonderie:
    
    def __init__ (self, tole : Tole, client : Client, cout : float, dict_all : dict[Materiau]):
        self._tole = tole
        self._client = client
        self._cout = cout
        self._dict_mat = dict_mat

    def get_tole(self):
        '''toles produites'''
        return self._tole
    
    def get_z(self):
        '''épaisseur demandée par le client (cm)'''
        return client.get_z(self._client)
    
    def get_cout(self):
        '''cout engendré par la fonte du métal et le laminage (€/cm^3)'''
        return self._cout
    
    def get_dict_mat(self):
        '''liste des matériaux '''
        return self._dict_mat

    def produire_plaque(self):
         """meme si fournisseurs dispo: faire avec  fonderie interne: payer totalelnt matieres premieres meme si stock de matiere premiere suffisant"""
        
        
