import math
from typing import List, Tuple, Union
import Plaques

import random

def solution1(data):
    plaque = data.copy()
    solution=[]
    for _ in range(len(data)):
        indice_plaque=random.randint(0,len(plaque)-1)
        polygone=plaque[ indice_plaque]
        pointd=random.randint(0,len(polygone))
        polygone_reordonne = polygone[pointd:] + polygone[:pointd]
        solution.append(polygone_reordonne)
        plaque.remove(polygone)
    return solution




def masse_metaux(self, nb_toles, tole_x, tole_y, tole_z, alliage):
    volume=nb_toles*tole._x*tole._y*tole.z"""cm^3"""
    mv=alliage.get_mv()"""pas sur """#en g/cm^3
    pct =alliage.get_list_pct()
    masse=[]
    for i in range(len(mv)):
        masse_metal_i=volume*mv[i]*pct[i]/1000
        masse.append(masse_metal_i)
    return masse
        
def cout_production_tole(self, nb_toles, tole_x, tole_y, tole_z, alliage, cout_fonte):
    cout_decoupe=self._prix_d*self.surface()
    volume=tole._x*tole._y*tole._z"""pour une tole cm^3"""
    cout_matiere_par_tole=alliage.prix_cm3()*volume
    cout_fonte_par_tole = cout_fonte*volume
    cout_total= nb_toles*(cout_decoupe +cout_matiere_par_tole + cout_fonte_par_tole)
 
    return cout_total

    
def tourner_plaque(self, tole_x, tole_y):
    """renvoi  plaque tournee ou pas"""
    nouvelle_rotation = self.ini_rotation_plaque()
    for i in range(len(nouvelle_rotation)):
        if self.rentre_dedans(tole_x, tole_y)==False:
        """ La plaque ne rentre pas: on la tourne (on met tout à 1 pour cette figure)"""
        
            
            nouvelle_rotation[i] = 1
            return Plaque(self._y, self._x, self._dict_p, self._prix_d,self._tole, self._qte_tole, nouvelle_rotation)
        else:
            return Plaque(self._x, self._y, self._dict_p, self._prix_d,self._tole, self._qte_tole, nouvelle_rotation)



def solution1(self):
    cout_total=cout_production_tole(self, nb_toles, tole_x, tole_y, tole_z, alliage, cout_fonte)
    masse_metal_toltale=masse_metaux(self, nb_toles, tole_x, tole_y, tole_z, alliage)
    fournisseur=0
    masse_alliage=0
    ligne_sol_1=[]
    qte_tole=[]
    
    for i in range(len(list_f):
        ligne_sol_1.append(j,list_f[i],0,0,Plaques.rotation_plaque[i]())
    return cout_total,masse_metal_toltale,fournisseur,masse_alliage,ligne_sol_1
    
    
    

    
     
