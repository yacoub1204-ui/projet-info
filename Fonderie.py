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
        """ 1.  metaux avec min = max  prioritare
          2. Tous les autres metaux partent de leur minimum.
          3. Le reliquat (1 - somme actuelle) est distribué sur les metaux libres (min < max),
             en remplissant chacun jusqu'a son maximum jusqu'a epuisement du reliquat.
        :return: liste de proportions (une par metal), somme = 1"""
        list_min = self._client.get_list_min()
        list_max = self._client.get_list_max()
        n = len(list_min)
 
        # Etape 1 : tous les metaux partent de leur minimum
        pct = list_min[:]
 
        # Etape 2 : reperer les metaux libres (min < max), les fixes sont deja corrects
        indices_libres = [i for i in range(n) if list_min[i] < list_max[i]]
 
        # Etape 3 : calculer le reliquat a distribuer sur les metaux libres
        reliquat = 1.0 - sum(pct)
 
        for i in indices_libres:
            absorbable = list_max[i] - pct[i]   # marge disponible pour ce metal
            ajout = min(reliquat, absorbable)
            pct[i] += ajout
            reliquat -= ajout
            if reliquat <= 1e-9:                 # reliquat nul (tolerance flottant)
                break
 
        assert reliquat <= 1e-9, \
            f"Impossible de satisfaire le cahier des charges (reliquat = {reliquat})"
 
        return pct
        
    def mv_alliage(self,pct):
        inverse_mv = sum(pct[i] / self._mv_metaux[i] for i in range(len(pct)))
        return 1/ inverse_mv
        
    def cout trivial(self, nb_toles):
        pct=self.pct_triviaux()
        volume_total_cm3 = nb_toles * self._x * self._y * self._client.get_z()
 
        # Masse totale de metal necessaire (g -> kg)
        mv = self.mv_alliage(pct)
        masse_totale_kg = volume_total_cm3 * mv / 1000.0
 
        # Repartition par metal et cout d'achat
        kg_par_metal = [masse_totale_kg * pct[i] for i in range(len(pct))]
        cout_achat = sum(kg_par_metal[i] * self._prix_metaux[i] for i in range(len(pct)))
 
        # Cout de fonte et laminage
        cout_fonte = volume_total_cm3 * self._cout_cm3
 
        cout_total = cout_achat + cout_fonte
        return cout_total, pct, kg_par_metal
    
    
 
        
    
    def creer_taule(self, t : int):
        '''permet de créer une taule venant de la fonderie'''
        tole = self._tole[t]
        cout = self._client.get_x * self._client.get_y * self._client.get_z * (self._client.prix_cm3 + self._cout)
        self._list_kg[t] -= 
