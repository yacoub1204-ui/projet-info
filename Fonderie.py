import Alliage
import Tole
import Client

class Fonderie:
    
    def __init__ (self, tole : list[Tole], list_all : list[Alliage], client : Client, list_kg : list[float], cout):
        self._tole = tole
        self._client = client
        self._cout = cout
        self._list_all = list_all
        self._list_kg = list_kg

    def get_tole(self):
        '''liste des toles produites'''
        return self._tole
    
    def get_z(self):
        '''épaisseur demandée par le client (cm)'''
        return self._client.get_z()
    
    def get_cout(self):
        '''cout engendré par la fonte du métal et le laminage (€/cm^3)'''
        return self._cout
    
    def get_list_kg(self):
        '''liste des masses d'alliage 1 et 2 disponibles'''
        return self._list_kg
    
    def get_list_all(self):
        '''liste des alliages possibles'''
        return self._list_all
    
    def creer_taule(self, t : int):
        '''permet de créer une taule venant de la fonderie'''
        tole = self._tole[t]
        cout = self._client.get_x * self._client.get_y * self._client.get_z * (self._client.prix_cm3 + self._cout)
        self._list_kg[t] -= 
