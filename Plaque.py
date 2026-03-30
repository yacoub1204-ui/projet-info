"""import Polygone

class Plaque:

    def __init__(self, prix_d : float, dict_p : dict[Polygone]):
        self._prix_d = prix_d
        self._dict_p = dict_p

    def get_prix_d(self):
        return self._prix_d
    
    def get_dict_p(self):
        return self._dict_p"""


import Polygone

class Plaque:

    def __init__(self, x: float, y: float, dict_p: dict[Polygone], prix_d: float,tole: list[str],qte_tole:list[(str,int)],rotation_plaque):""" tole et qte_tole pour savoir quelle figure on cree et quelle quantite de cette figure on produit car c des listes. Exemple: tole[i]=bateau et qte_tole[i]=(bateau,3)              rotation_plaque[i][j]=1car la j-eme plaque bateau(figure d'indice i) est tournee(car c 1, 0 si pas tournee) """
        self._x=x                                                                                                                                                                                                                                                                                                           """  rotation_plaque=[[0,1,0],[0,0,0,0,1,1,1,0]] la premiere liste represente les plaques bateaux tournees et la deuxieme les plaques dune autre figure tournee"""                                       
        self._y=y
        self._prix_d = prix_d """euro/cm^2"""
        self._dict_p = dict_p
        self._tole=tole
        self._qte_tole=qte_tole
        self._rotation_plaque = rotation_plaque


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_prix_d(self):
        return self._prix_d
    
    def get_dict_p(self):
        return self._dict_p

    def get_tole(self):
        return self._tole

    def get_qte_tole(self):
        return self._qte_tole

    def get_rotation_plaque(self):
        return self._rotation_plaque

    def surface(self):
        return self._x*self._y

    def rentre_dedans(self, tole_x, tole_y):
        return self._x <=tole_x and self._y<= tole_y


    
    def cout_decoupe(self):
        return self._prix_d*self.surface
        

    def ini_rotation_plaque(self):
        ini_rotation=[]
        for i in range(len(self._tole)):
            nb_exemplaires = self._qte_tole[i][1]# qte_tole[i] = (nom de la figure, quantite)
            ini_rotation.append([0] for j in range(nb_exemplaire))
        return ini_rotation
        



    
    def rentre_dedans(self, tole_x,tole_y):
    """renvoie booléen"""
        return self.x<=tole_x and self._y <= tole_y


    def tourner_plaque(self, tole_x, tole_y):
        """renvoi  plaque tournee ou pas"""
        nouvelle_rotation = self.ini_rotation_plaque()
        if self.rentre_dedans(tole_x, tole_y)==False:
            """ La plaque ne rentre pas: on la tourne (on met tout à 1 pour cette figure)"""
            for i in range(len(nouvelle_rotation)):
                for j in range(len(nouvelle_rotation[i])):
                    nouvelle_rotation[i][j] = 1
            return Plaque(self._y, self._x, self._dict_p, self._prix_d,
                          self._tole, self._qte_tole, nouvelle_rotation)
        else:
            return Plaque(self._x, self._y, self._dict_p, self._prix_d,
                          self._tole, self._qte_tole, nouvelle_rotation)

    def masse_metaux(self, nb_toles, tole_x, tole_y, tole_z, alliage):
        volume=nb_tole*tole._x*tole._y*tole.z"""cm^3"""
        mv=alliage.get_mv()"""pas sur """#en g/cm^3
        pct =alliage.get_list_pct()
        masse=[]
        for i in range(len(mv)):
            masse_metal_i=volume*mv[i]*pct[i]/1000
            masse;append(masse_metal_i)
        return masse
        
        

    def cout_decoupe(self):
        return self._prix_d*self.surface()

