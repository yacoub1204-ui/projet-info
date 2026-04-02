import Plaques
import Figure
import Tole



#prerequis autresclasses

class Placement:
    def __init__(self, figure: Figure, x_origine, y_origine, tournee):
        self._figure = figure
        self._x = x_origine"""coordonnees du coin en bas a gauche de la plaque"""
        self._y= y_origine
        self._tournee=tournee

class TolePlan:
    def __init__(self, tole:Tole):
        self._tole = tole
        self._placements = [] """Placement(figure, x_origine,y_origine,tournee)"""
                            """liste des plaques decoupees dans toles"""

class Solution:
    def __init__(self):
        self.plans = [] #liste de Tolplan

    def afficher(self):
        for i, plan in enumerate(self.plans):
            print(f"\n--- Tôle {i+1} ---")
            for p in plan.placements:
                print(p)



# Classe espace libre

class EspaceLibre:
    def __init__(self, x, y, lx, ly):
        self._x = x"""position espace libre"""
        self._y = y
        self._lx = lx"""espace libre largeur"""
        self._ly = ly

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_lx(self):
        return self._lx
    def get_ly(self):
        return self._ly

    def surface_libre(self):
        return self._lx * self._ly

    def rentre_dedans(self,Figure):
        return figure.get_x() <= self._lx and figure.get_y() <= self._ly

    def gaspillage(self):
        return self.surface_libre - self._lx *self._ly
        
#alg decoupe
def _decouper_guillotine(espace: EspaceLibre, figure: Figure, tournee: bool):"""espace sans s"""
    reste = []
    if tournee==True:
        fx= figure.get_y() # largeur figure/plaque placée
        fy = figure.get_x() 
    else:
        fx= figure.get_x() 
        fy = figure.get_y() 
        
    r_x = espace.get_lx() - fx """reste en x"""
    r_y = espace.get_ly() - fy

    if r_x >= r_y: """coupe horizontale-> grand espace en haut"""
        if r_y > 0:
            reste.append(EspaceLibre(espace.x, espace.y + fy, espace.lx, r_y))
        if r_x > 0:
            reste.append(EspaceLibre(espace.x + fx, espace.y, r_x, fy))
    else:"""coupe verticale -> grand espace a droite"""
        if r_x > 0:
            reste.append(EspaceLibre(espace.x + fx, espace.y, r_x, espace.ly))
        if r_y > 0:
            reste.append(EspaceLibre(espace.x, espace.y + fy, fx, r_y))

    resultat = []
    for espace in reste:
        if espace.surface_libre() > 0:
            resultat.append(espace)

    return resultat



def _meilleur_placement(espaces: list[EspaceLibre], figure: Figure,autoriser_rotation: bool)): """espaces avec un s"""
    meilleur = None                                                   """autoriser_rotation defini dans decouper"""
    meilleur_gasp = float('inf')
    fx=figure.get_x()
    fy=figure.get_y()
    orientations = [(fx, fy)]
    if autoriser_rotation and fx != fy:
        orientations.append((fy, fx))

    meilleur = None
    meilleur_gasp = float('inf')
    indice = 0
    for espace in espaces:
        for orientation in orientations:
            largeur = orientation[0]
            hauteur = orientation[1]
            if espace.peut_accueillir(largeur, hauteur):
                gaspillage = espace.gaspillage(largeur, hauteur)
                if gaspillage < meilleur_gasp:
                    meilleur = (indice, largeur, hauteur)
                meilleur_gasp = gaspillage
        indice += 1
    return meilleur

#algo principal
def decouper(tole: Tole, plaques: Plaques, autoriser_rotation: bool = True):#return une solution avec les Toleplan et leurs Placements

    figures = sorted(plaques.get_list_f(),key=lambda f: f.get_x()* f.get_y(),reverse=True)

    solution = Solution()
    plans_espaces = []    #plans_espaces[i]= list[EspaceLibre] pour la tole i

    for figure in figures:
        fx, fy = figure.get_x(), figure.get_y()

        resultat = None
        tole_idx = None

        # ── 1. Best-Fit sur TOUTES les tôles ouvertes ──────────────────
        meilleur_score = -1.0
        for i, espaces in enumerate(plans_espaces):
            res = _meilleur_placement(espaces, figure, autoriser_rotation)
            if res:
                surf_tole = tole.get_x() * tole.get_y()
                surf_deja = sum(
                    p.figure.get_x() * p.figure.get_y()
                    for p in solution.plans[i].placements
                )
                score = (surf_deja + res[1] * res[2]) / surf_tole
                if score > meilleur_score:
                    meilleur_score = score
                    resultat  = res
                    tole_idx  = i
 
        # ── 2. Tentative de fusion avant d'ouvrir une nouvelle tôle ────
        if resultat is None:
            for i, espaces in enumerate(plans_espaces):
                espaces_fus = _fusionner_espaces(espaces)
                if espaces_fus is not espaces:
                    res = _meilleur_placement(espaces_fus, figure, autoriser_rotation)
                    if res:
                        plans_espaces[i] = espaces_fus
                        resultat = res
                        tole_idx = i
                        break
 
        # ── 3. Nouvelle tôle en dernier recours ─────────────────────────
        if resultat is None:
            tole_idx    = len(solution.plans)
            espace_init = EspaceLibre(0, 0, tole.get_x(), tole.get_y())
            plans_espaces.append([espace_init])
            solution.plans.append(TolePlan(tole))
 
            resultat = _meilleur_placement(
                plans_espaces[tole_idx], figure, autoriser_rotation
            )
            if resultat is None:
                fx_nom: float = figure.get_x()  # largeur nominale de la figure
                fy_nom: float = figure.get_y()  # hauteur nominale de la figure
                raise ValueError(
                    f"Figure {figure} ({fx_nom}×{fy_nom}) trop grande "
                    f"pour la tôle ({tole.get_x()}×{tole.get_y()})"
                )
 
        # ── 4. Placement ────────────────────────────────────────────────
        esp_idx, fx_eff, fy_eff = resultat
        esp = plans_espaces[tole_idx][esp_idx]
 
        # tournee = True si la figure a été pivotée à 90° (fx_eff correspond à get_y())
        tournee: bool = (fx_eff != figure.get_x())
 
        solution.plans[tole_idx].placements.append(
            Placement(figure, esp.get_x(), esp.get_y(), tournee=tournee)
        )
 
        # Découpe guillotine + mise à jour des espaces
        reste = _decouper_guillotine(esp, figure, tournee)
        plans_espaces[tole_idx].pop(esp_idx)
        plans_espaces[tole_idx].extend(reste)
        plans_espaces[tole_idx].sort(key=lambda e: e.surface_libre, reverse=True)
 
    return solution

        
   


                    
            
