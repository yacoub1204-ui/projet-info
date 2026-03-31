
import Plaques
import Figure
import Tole



def def_plaque(plaques.get_list_f(),figure.get_x(),figure.get_y()):
""" a la fin j'aurai plaque=[("bateau",x=6,y=12),("etoile",x=9,y=3)]"""
    plaque=[]
    for i in range(plaques.get_list_f()):
        plaque.apppend(plaques.get_list_f[i](),figure.get_x(),figure.get_y())
    return plaque


"""on sait que dans fichier tole on a :

    def __init__(self, x, y, z, all : Alliage"""
def surface_tole_restante(self):
    toles_utilisees=0
    tole=(self.x,self.y)
    toutes_plaques=def_plaque(plaques.get_list_f(),figure.get_x(),figure.get_y())
    plaques_restantes=toutes_plaques.copy()
    
    plaques_crees=[]
    While plaques_restantes:
        if self.x*self.y>=figure.get_x*figure.get_y:
            for i in range(len(toutes_plaques)):
                if plaque.rentre_dedans(toutes_plaques[i], tole.get_x(), tole.get_y(),self.x,self.y):
                    plaques_crees.append(toutes_plaques[i])
                    plaques_restantes.remove(plaques.get_list_f,figure.get_x(),figure.get_y())
                    tole_part_bas=(tole[0]-figure.get_x(),figure.get_y())
                    tole_part_haut=(tole[0],tole[1]-figure.get_y())
                    tole=[tole_part_bas,tole_part_haut]
        toles_utilisees+=1
        tole=(self.x,self.y)

    return toles_utilisees, 
                    
                    
            
