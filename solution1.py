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




def masse_metaux(plaques, tole : Tole, alliage):
    volume=sum(tole.get_x()*tole.get_y()*tole.get_z() for i in range(len(plaques.get_list_f()))"""cm^3"""
    mv=alliage.get_mv()"""pas sur """#en g/cm^3
    pct =alliage.get_list_pct()
    masse=[]
    for i in range(len(plaques.get_list_f())):
        masse_metal_i=volume*mv[i]*pct[i]/1000
        masse.append(masse_metal_i)
    return masse
        
def cout_production_tole(plaques, tole, alliage, cout_fonte):
    cout_decoupe=plaques.get_prix_d()*plaques.get_surface()
    volume=tole.get_x()*tole.get_y()*tole.get_z()"""pour une tole cm^3"""
    cout_matiere_par_tole=alliage.get_prix_cm3()*volume
    cout_fonte_par_tole = cout_fonte*volume
    cout_total= nb_toles*(cout_decoupe +cout_matiere_par_tole + cout_fonte_par_tole)
 
    return cout_total

    
def tourner_plaque(plaques, tole):
    """renvoi  plaque tournee ou pas"""
    nouvelle_rotation = plaques.get_ini_rotation_plaque()
    for i in range(len(plaques.get_list_f())):
        if plaques.get_rentre_dedans(tole.get_x(), tole.get_y())==False:
        """ La plaque ne rentre pas: on la tourne (on met tout à 1 pour cette figure)"""
        
            
            nouvelle_rotation[i] = 1
            return Plaques(self, self._dict_p, self._prix_d,list_f, rotation_plaque)
        else:
            return Plaques(self, self._dict_p, self._prix_d,list_f, rotation_plaque)



def solution1(plaques,tole, alliage, cout_fonte):
    cout_total=cout_production_tole(plaques, tole, alliage, cout_fonte)
    masse_metal_toltale=masse_metaux(plaques, tole, alliage)
    fournisseur=0
    masse_alliage=0
    ligne_sol_1=[]
    qte_tole=[]
    
    for i in range(len(plaques.get_list_f())):
        ligne_sol_1.append(i,plaques.get_list_f[i](),0,0,plaques.get_rotation_plaque[i]())
    solution_1=cout_total,masse_metal_toltale,fournisseur,masse_alliage,ligne_sol_1
    return solution_1
    
    
    

    
     
