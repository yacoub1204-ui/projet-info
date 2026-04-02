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



class _EspaceLibre:
    """Rectangle libre dans une tôle (coin bas-gauche + dimensions)."""
    x  : float
    y  : float
    lx : float   # largeur disponible
    ly : float   # hauteur disponible

    @property
    def surface(self) -> float:
        return self.lx * self.ly

    def peut_accueillir(self, fx: float, fy: float) -> bool:
        return fx <= self.lx and fy <= self.ly

    def gaspillage(self, fx: float, fy: float) -> float:
        """Surface perdue si on place une figure fx×fy dans cet espace."""
        return self.surface - fx * fy


# ══════════════════════════════════════════════════════════════════════════════
#  Découpe guillotine d'un espace après placement
# ══════════════════════════════════════════════════════════════════════════════

def _decouper_guillotine(espace: _EspaceLibre,
                         fx: float, fy: float) -> list[_EspaceLibre]:
    """
    Après avoir placé une figure fx×fy dans `espace`, génère les restes.

    Stratégie « découpe par le long côté » :
    - Si la largeur restante > la hauteur restante → coupe horizontale
    - Sinon → coupe verticale
    Cela produit des reste aussi carrés que possible (plus faciles à remplir).

    Schéma (coupe horizontale) :
        ┌───────────────────┐
        │  haut (lx × r_y)  │
        ├──────┬────────────┤
        │ fig  │bas (r_x×fy)│
        └──────┴────────────┘
    """
    reste = []
    r_x = espace.lx - fx   # largeur restante à droite
    r_y = espace.ly - fy   # hauteur restante au-dessus

    if r_x >= r_y:
        # Coupe horizontale : reste en  haut sur toute la largeur
        if r_y > 0:
            reste.append(_EspaceLibre(espace.x, espace.y + fy, espace.lx, r_y))
        if r_x > 0:
            reste.append(_EspaceLibre(espace.x + fx, espace.y, r_x, fy))
    else:
        # Coupe verticale : reste a droite sur toute la hauteur
        if r_x > 0:
            reste.append(_EspaceLibre(espace.x + fx, espace.y, r_x, espace.ly))
        if r_y > 0:
            reste.append(_EspaceLibre(espace.x, espace.y + fy, fx, r_y))

    return [r for r in reste if r.surface > 0]


# ══════════════════════════════════════════════════════════════════════════════
#  Recherche du meilleur placement pour une figure
# ══════════════════════════════════════════════════════════════════════════════

def _meilleur_placement(espaces: list[_EspaceLibre],
                        fx: float, fy: float,
                        autoriser_rotation: bool
                        ) -> tuple[int, float, float] | None:
    """
    Cherche parmi tous les espaces celui qui minimise le gaspillage.

    Retourne (indice_espace, fx_effectif, fy_effectif) ou None.
    fx_effectif / fy_effectif tiennent compte de la rotation éventuelle.
    """
    meilleur_idx   = None
    meilleur_gasp  = float('inf')
    meilleur_fx    = fx
    meilleur_fy    = fy

    orientations = [(fx, fy)]
    if autoriser_rotation and fx != fy:
        orientations.append((fy, fx))   # rotation 90 deg

    for i, esp in enumerate(espaces):
        for ex, ey in orientations:
            if esp.peut_accueillir(ex, ey):
                gasp = esp.gaspillage(ex, ey)
                if gasp < meilleur_gasp:
                    meilleur_gasp  = gasp
                    meilleur_idx   = i
                    meilleur_fx    = ex
                    meilleur_fy    = ey

    if meilleur_idx is None:
        return None
    return meilleur_idx, meilleur_fx, meilleur_fy


# ══════════════════════════════════════════════════════════════════════════════
#  Algorithme principal
# ══════════════════════════════════════════════════════════════════════════════

def decouper(tole, plaques, autoriser_rotation: bool = True) -> Solution:
    """
    Algorithme Guillotine Best-Fit Décroissant (GBFD).

    Paramètres
    ----------
    tole : Tole
        Gabarit de tôle (x, y, z, alliage).
    plaques : Plaques
        Ensemble des figures à découper.
    autoriser_rotation : bool
        Si True, chaque figure peut être pivotée de 90°.

    Retourne
    --------
    Solution
        Plan complet de découpe avec positions et rotations.
    """
    # 1. Récupérer les figures et les trier par surface décroissante
    figures = sorted(
        plaques.get_list_f(),
        key=lambda f: f.get_x() * f.get_y(),
        reverse=True
    )

    solution = Solution()
    plans_espaces: list[list[_EspaceLibre]] = []  # espaces libres par tôle

    for figure in figures:
        fx, fy = figure.get_x(), figure.get_y()

        # 2. Chercher un espace dans les tôles déjà ouvertes
        resultat = None
        tole_choisie_idx = None

        for t_idx, espaces in enumerate(plans_espaces):
            res = _meilleur_placement(espaces, fx, fy, autoriser_rotation)
            if res is not None:
                # Préférer la tôle la plus remplie (indice le plus bas = plus ancienne)
                resultat = res
                tole_choisie_idx = t_idx
                break   # first-fit sur les tôles, best-fit sur les espaces

        # 3. Aucune tôle existante ne convient → ouvrir une nouvelle tôle
        if resultat is None:
            tole_choisie_idx = len(solution.plans)
            espace_initial   = _EspaceLibre(0, 0, tole.get_x(), tole.get_y())
            plans_espaces.append([espace_initial])
            solution.plans.append(TolePlan(tole=tole))
            resultat = _meilleur_placement(
                plans_espaces[tole_choisie_idx], fx, fy, autoriser_rotation
            )
            if resultat is None:
                raise ValueError(
                    f"La figure {figure} ({fx}×{fy}) ne tient pas dans une tôle "
                    f"({tole.get_x()}×{tole.get_y()}). Vérifiez les dimensions."
                )

        # 4. Enregistrer le placement
        esp_idx, fx_eff, fy_eff = resultat
        esp = plans_espaces[tole_choisie_idx][esp_idx]
        tournee = (fx_eff != fx)

        placement = Placement(
            figure   = figure,
            x_offset = esp.x,
            y_offset = esp.y,
            tournee  = tournee
        )
        solution.plans[tole_choisie_idx].placements.append(placement)

        # 5. Découpe guillotine : remplacer l'espace utilisé par ses reste
        reste = _decouper_guillotine(esp, fx_eff, fy_eff)
        plans_espaces[tole_choisie_idx].pop(esp_idx)
        plans_espaces[tole_choisie_idx].extend(reste)

        # Trier les espaces par surface décroissante (best-fit plus rapide)
        plans_espaces[tole_choisie_idx].sort(key=lambda e: e.surface, reverse=True)

    return solution



                    
            
