import math
from typing import List, Tuple, Union
import Plaques

import random

"""def solution1(data):
    plaque = data.copy()
    solution=[]
    for _ in range(len(data)):
        indice_plaque=random.randint(0,len(plaque)-1)
        polygone=plaque[ indice_plaque]
        pointd=random.randint(0,len(polygone))
        polygone_reordonne = polygone[pointd:] + polygone[:pointd]
        solution.append(polygone_reordonne)
        plaque.remove(polygone)
    return solution"""



def solution1(plaques,tole, alliage, cout_fonte):
    cout_total=plaques.cout_production_tole(plaques, tole, alliage, cout_fonte)
    masse_metal_toltale=plaques.masse_metaux(plaques, tole, alliage)
    fournisseur=0
    masse_alliage=[0 for i in range(len(tole.get_list_all()))]
    ligne_sol_1=[]
    
    
    for i in range(len(plaques.get_list_f())):
        ligne_sol_1.append(i,plaques.get_list_f[i](),0,0,plaques.get_rotation_plaque[i]())
    solution_1=cout_total,masse_metal_toltale,fournisseur,masse_alliage,ligne_sol_1
    return solution_1
    
    
    

    
     
