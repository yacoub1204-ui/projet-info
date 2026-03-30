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

"""    def nb_tole(self): #nombre tole produites
        nb_tole=len(tole)
        return nb_tole    """
    
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

    def get_client(self):
        return self._client


    def pct_triviaux(self) -> list[float]:
       """1.  metaux avec min = max  prioritare
          2. Tous les autres metaux partent de leur minimum.
          3. pour  la condition " somme pct metaux =1" il faut distribuer le reste des pct sur les metaux libres (min < max),
             en remplissant chacun jusqu'a son maximum jusqu'a somme pct metal egale a 1."""
        list_min = self._client.get_list_min()
        list_max = self._client.get_list_max()
        n = len(list_min)
 
        # Etape 1 : tous les metaux partent de leur minimum
        pct = list_min.copy()
 
        # Etape 2 : reperer les metaux libres (min < max), les fixes sont deja corrects
        indices_libres = [i for i in range(n) if list_min[i] < list_max[i]]
 
        # Etape 3 : calculer le reste de pourcentage a distribuer sur les metaux libres
        reste = 1 - sum(pct)
 
        for i in indices_libres:
            absorbable = list_max[i] - pct[i]   # marge disponible pour ce metal
            ajout = min(reste, absorbable)
            pct[i] += ajout
            reste -= ajout
            if reste <= 1e-9:                 # reste nul (petie tolerance)
                break
        return pct
        
    def masse_volumique(self, pct, mv_metaux):
        """masse volumique alliage."""
        somme = 0
        for i in range(len(pct)):
            somme += pct[i] / mv_metaux[i]

        return 1 / somme
        
    def calcul_cout(self, nb_toles, mv_metaux, prix_metaux):
        """coût total de production."""
        pct = self.calcul_pourcentages()
        # volume total
        volume = nb_toles * self.client.get_x() * self.client.get_y() * self.client.get_z()
        # masse volumique
        mv = self.masse_volumique(pct, mv_metaux)
        # masse totale (kg)
        masse = volume * mv / 1000
        # coût des métaux
        cout_metaux = 0
        for i in range(len(pct)):
            cout_metaux += masse * pct[i] * prix_metaux[i]
        # coût fabrication
        cout_fabrication = volume * self.cout_cm3
        cout_total = cout_metaux + cout_fabrication
        return cout_total




    def solution_fonderie(self):
        cout_prod=sum(calcul_cout(self, nb_tole, mv_metaux, prix_metaux) for i in range(len(figures)) """figures c le dictionnaire repertorant les differentes figures a produire"""
        """nb_tole est le nombre de tole (donc de plaque) a produire pour solution triviale. Il faut un nb_tole par type de figure"""
        fournisseur=0 #fonderie
        nb_tole_final=len(self.tole)
        masse_metal_cree=[mv_metaux*pct[i]*nb_toles * self.client.get_x() * self.client.get_y() * self.client.get_z()/1000 for i in range(len(list_min))
        masse_metal_stock_utilise=[ 0 for i in range(len(list_all_stock))]"""jsp si une variable repertoriant les alliages en stock existe"""
        ligne_prod=[]
        rotation_plaque=0
        for i in range(len(nb_tole_final)):
        
            if rotation(plaque[i][1])=1: # parametres a refaire
                rotation_plaque=1
        
            ligne_prod[i]= [i,tole[i],0,0,rotation_plaque] # memoire de rotation pour chaque plaque a faire dans plaque.py
    
    
 
        
    
    def creer_taule(self, t : int):
        '''permet de créer une taule venant de la fonderie'''
        tole = self._tole[t]
        cout = self._client.get_x * self._client.get_y * self._client.get_z * (self._client.prix_cm3 + self._cout)
        self._list_kg[t] -= 
