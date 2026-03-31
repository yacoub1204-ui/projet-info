import Polygone

class Plaques:

    def __init__(self, prix_d : float, list_f : list[Figures], rotation_plaque):
        self._prix_d = prix_d
        self._list_f = list_f
        self._rotation_plaque = rotation_plaque

    def get_prix_d(self):
        """renvoie le prix du déplacement du laser"""
        return self._prix_d
    
    def get_list_f(self):
        """renvoie la liste contenant toutes les figures à découper dans chaque plaque"""
        return self._list_f


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
    

    def rentre_dedans(self, tole_x, tole_y):
        """renvoie booléen"""
        return self.x<=tole_x and self._y <= tole_y


    def tourner_plaque(self, tole.get_x(), tole.get_y()):
        """renvoi  plaque tournee ou pas"""
        nouvelle_rotation = self.ini_rotation_plaque()
        for i in range(len(list_f)):
            if self.rentre_dedans(tole.get_x(), tole.get_y())==False:
            """ La plaque ne rentre pas: on la tourne (on met tout à 1 pour cette figure)"""
                        
                    nouvelle_rotation[i] = 1
                return Plaque(self, self._dict_p, self._prix_d,self._list_f, nouvelle_rotation)
            else:
                return Plaque(self, self._dict_p, self._prix_d,self._list_f, nouvelle_rotation)


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
        cout_decoupe=plaques.get_prix_d()*plaques.surface()
        volume=tole.get_x()*tole.get_y()*tole.get_z()"""pour une tole cm^3"""
        cout_matiere_par_tole=alliage.get_prix_cm3()*volume
        cout_fonte_par_tole = cout_fonte*volume
        cout_total= nb_toles*(cout_decoupe +cout_matiere_par_tole + cout_fonte_par_tole)
 
        return cout_total
    



