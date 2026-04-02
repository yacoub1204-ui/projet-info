import Plaques
import Figure
import Tole



def def_plaque(Plaques, Figure, Tole):
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



#methode 2 test pas finos


"""Algorithme de découpe 2D optimisé : Guillotine Best-Fit Décroissant (GBFD).
Principe:
1. Trier les figures par surface décroissante (les plus grandes d'abord).
2. Pour chaque figure, essayer les deux orientations (normale et +90°).
3. Parmi tous les espaces libres disponibles, choisir celui qui minimise
   le gaspillage (surface restante après découpe).
4. Découpe guillotine : l'espace choisi est scindé en deux restes
   (bas et droite). On conserve le plus grand en premier.
5. Si aucun espace ne convient, ouvrir une nouvelle tôle.

First-Fit Guillotine

- BFD    : grandes pièces en premier → moins de fragmentation des espaces.
- Best-Fit : on choisit l'espace le moins gaspillé → espaces restants plus utiles.
- Rotation : augmente les chances de placement sans nouvelle tôle."""

#from __future__ import annotations
#from dataclasses import dataclass, field
#from Solution import Placement, TolePlan, Solution


#prerequis dans les autresclasses
class Figure:
    def __init__(self, x, y, nom=""):
        self.x = x
        self.y = y
        self.nom = nom

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return f"{self.nom}({self.x}x{self.y})"



class Plaques:
    def __init__(self, figures):
        self.figures = figures

    def get_list_f(self):
        return self.figures



class Tole:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


#classe pour solution
class Placement:
    def __init__(self, figure, x_offset, y_offset, tournee):
        self.figure = figure
        self.x = x_offset
        self.y = y_offset
        self.tournee = tournee

    def __repr__(self):
        rot = " (rot)" if self.tournee else ""
        return f"{self.figure} placé en ({self.x},{self.y}){rot}"


class TolePlan:
    def __init__(self, tole):
        self.tole = tole
        self.placements = []

    def __repr__(self):
        return f"Tole {self.tole.get_x()}x{self.tole.get_y()} -> {self.placements}"


class Solution:
    def __init__(self):
        self.plans = []

    def afficher(self):
        for i, plan in enumerate(self.plans):
            print(f"\n--- Tôle {i+1} ---")
            for p in plan.placements:
                print(p)



# Classe espace libre

class _EspaceLibre:
    def __init__(self, x, y, lx, ly):
        self.x = x
        self.y = y
        self.lx = lx
        self.ly = ly

    @property
    def surface(self):
        return self.lx * self.ly

    def peut_accueillir(self, fx, fy):
        return fx <= self.lx and fy <= self.ly

    def gaspillage(self, fx, fy):
        return self.surface - fx * fy


#alg decoupe
def _decouper_guillotine(espace, fx, fy):
    reste = []
    r_x = espace.lx - fx
    r_y = espace.ly - fy

    if r_x >= r_y:
        if r_y > 0:
            reste.append(_EspaceLibre(espace.x, espace.y + fy, espace.lx, r_y))
        if r_x > 0:
            reste.append(_EspaceLibre(espace.x + fx, espace.y, r_x, fy))
    else:
        if r_x > 0:
            reste.append(_EspaceLibre(espace.x + fx, espace.y, r_x, espace.ly))
        if r_y > 0:
            reste.append(_EspaceLibre(espace.x, espace.y + fy, fx, r_y))

    return [r for r in reste if r.surface > 0]



def _meilleur_placement(espaces, fx, fy, autoriser_rotation):
    meilleur = None
    meilleur_gasp = float('inf')

    orientations = [(fx, fy)]
    if autoriser_rotation and fx != fy:
        orientations.append((fy, fx))

    for i, esp in enumerate(espaces):
        for ex, ey in orientations:
            if esp.peut_accueillir(ex, ey):
                gasp = esp.gaspillage(ex, ey)
                if gasp < meilleur_gasp:
                    meilleur = (i, ex, ey)
                    meilleur_gasp = gasp

    return meilleur


#algo principal
def decouper(tole, plaques, autoriser_rotation=True):

    figures = sorted(
        plaques.get_list_f(),
        key=lambda f: f.get_x() * f.get_y(),
        reverse=True
    )

    solution = Solution()
    plans_espaces = []

    for figure in figures:
        fx, fy = figure.get_x(), figure.get_y()

        resultat = None
        tole_idx = None

        for i, espaces in enumerate(plans_espaces):
            res = _meilleur_placement(espaces, fx, fy, autoriser_rotation)
            if res:
                resultat = res
                tole_idx = i
                break

        if resultat is None:
            tole_idx = len(solution.plans)
            espace_init = _EspaceLibre(0, 0, tole.get_x(), tole.get_y())

            plans_espaces.append([espace_init])
            solution.plans.append(TolePlan(tole))

            resultat = _meilleur_placement(plans_espaces[tole_idx], fx, fy, autoriser_rotation)

            if resultat is None:
                raise ValueError("Figure trop grande pour la tôle")

        esp_idx, fx_eff, fy_eff = resultat
        esp = plans_espaces[tole_idx][esp_idx]

        placement = Placement(
            figure,
            esp.x,
            esp.y,
            tournee=(fx_eff != fx)
        )

        solution.plans[tole_idx].placements.append(placement)

        reste = _decouper_guillotine(esp, fx_eff, fy_eff)
        plans_espaces[tole_idx].pop(esp_idx)
        plans_espaces[tole_idx].extend(reste)

        plans_espaces[tole_idx].sort(key=lambda e: e.surface, reverse=True)

    return solution


# =========================
# TEST
# =========================
if __name__ == "__main__":

    figs = [
        Figure(5, 4, "A"),
        Figure(3, 3, "B"),
        Figure(6, 2, "C"),
        Figure(2, 2, "D"),
    ]

    plaques = Plaques(figs)
    tole = Tole(10, 10)

    sol = decouper(tole, plaques)

    sol.afficher()


                    
            
