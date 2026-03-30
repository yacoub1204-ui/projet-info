import Polygone

class Plaque:

    def __init__(self, x: float, y: float, dict_p: dict[Polygone], prix_d: float,tole: list[str],qte_tole:list[(str,int)],rotation_plaque):""" tole et qte_tole pour savoir quelle figure on cree et quelle quantite de cette figure on produit car c des listes. Exemple: tole[i]=bateau et qte_tole[i]=(bateau,3)              rotation_plaque[i][j]=1car la j-eme plaque bateau(figure d'indice i) est tournee(car c 1, 0 si pas tournee) """
        self._x=x                                                                                                                                                                                                                                                                                                           """  rotation_plaque=[[0,1,0],[0,0,0,0,1,1,1,0]] la premiere liste represente les plaques bateaux tournees et la deuxieme les plaques dune autre figure tournee"""                                       
        self.y=y
        self._prix_d = prix_d """euro/cm^2"""
        self._dict_p = dict_p


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_prix_d(self):
        return self._prix_d
    
    def get_dict_p(self):
        return self._dict_p

    def surface(self):
        return self._x*self._y


    def rotation(self,rotation_plaque):
        for i in range (len(rotation_plaque[i])):
            for j in range(len(rotation_plaque[i][j])):
                if  rentre_dedans(self, tole_x,tole_y)==False:
                    return Plaque(self._y,self._x,self._dict_p,self._prix_d,qte_tole:list[(str,int)],rotation_plaque[i][j]=1) 
                else:
                    return Plaque(self._y,self._x,self._dict_p,self._prix_d,qte_tole:list[(str,int)],rotation_plaque[i][j]=0) 
        



    def rentre_dedans(self, tole_x,tole_y):
    """renvoie booléen"""
        return self.x<=tole_x and self._y <= tole_y


    def cout_decoupe(self):
        return self._prix_d*self.surface()
