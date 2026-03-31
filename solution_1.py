import Plaques
import Figure
from random import randint
def solution_1(data):
    solution=[]
    for lines in data:
        number=randint(0,len(lines))
        solution.append()
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

def solution1(self):
    return 


