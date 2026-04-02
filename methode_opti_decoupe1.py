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
def _decouper_guillotine(espace: EspaceLibre, figure: Figure, tournee: bool):
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


                    
            
