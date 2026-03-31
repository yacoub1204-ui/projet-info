import Alliage

class Tole:

    def __init__(self, x, y, z, all : Alliage):
        self._x = x
        self._y = y
        self._z = z
        self._all = all

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_z(self):
        return self._z

    def get_all(self):
        return self._all

________________
#methode decoupe num 1
___________________

    def def_plaque(plaques, figures, Toles):
""" a la fin j'aurai plaque=[("bateau",x=6,y=12),("etoile",x=9,y=3)]"""
    plaque=[]
    for i in range(len(plaques.get_list_f())):
        plaque.append((plaques.get_list_f()[i],figure.get_x(),figure.get_y()))
    return plaque
#plaque.get_list_f()[i].get_x()=x de la figure d'indice i

"""on sait que dans fichier tole on a :

    def __init__(self, x, y, z, all : Alliage"""
    def surface_tole_restante(self, plaques,figure):
        toles_utilisees=0
        tole=Tole(self.x,self.y)
        toutes_plaques=def_plaque(plaques.get_list_f(),figure.get_x(),figure.get_y())
        plaques_restantes=toutes_plaques.copy()
        tole_dispo=[Tole(self.x,self.y)]#liste dee morceaux de tole
    
        plaques_crees=[]
        while plaques_restantes:
            if self.x*self.y>=figure.get_x()*figure.get_y():
                for i in range(len(toutes_plaques)):
                    if plaque.rentre_dedans(toutes_plaques[i], tole.get_x(), tole.get_y(),self.x,self.y):
                        plaques_crees.append(toutes_plaques[i])
                        plaques_restantes.remove((plaques.get_list_f(),figure.get_x(),figure.get_y()))
                        tole_part_bas=Tole(tole.x - figure.get_x(),figure.get_y())
                        tole_part_haut=Tole(tole.x,tole.y - figure.get_y())
                        tole=[tole_part_bas,tole_part_haut]
            toles_utilisees+=1
            tole=Tole(self.x,self.y)

        return toles_utilisees
                    
