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
    reste = []                                                                """decoupe un espace libre apres le placement d'un rectangle"""
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


def _fusionner_espaces(espaces: list[EspaceLibre]):
    """Tente de fusionner des paires d'espaces dont les intervalles x ou y
    se chevauchent pour créer un rectangle d'espace libre qui "traverse" les autres (et qui est plus grand)."""
    if len(espaces) < 2:
        return espaces
 
    utilises = utilises = [False] * len(espaces)  #utilises =set() marche est peut etre pllus pertinient
    nouveaux = []
 
    for i in range(len(espaces)):
        if utilises[i]==True:
            continue
        for j in range(i + 1, len(espaces)):
            if j in utilises:
                continue
 
            A= espaces[i]#rectangle coin inferieur gauche en x,y et largeur lx et hauteur ly
            B = espaces[j]
 
            # Fusion verticale : chevauchement en x, un rectangle avec un plus grand y est cree
            x_gauche = max(A.get_x(), B.get_x())#intervalle
            x_droit = min(A.get_x() + A.get_lx(), B.get_x() + B.get_lx())
            if x_droit - x_gauche > 0:
                y_bas = min(A.get_y(), B.get_y())
                y_haut = max(A.get_y() + A.get_ly(), B.get_y() + B.get_ly())
                fv = EspaceLibre(x_gauche, y_bas,
                                 x_droit - x_gauche, y_haut - y_bas)"""fv=fusion verticale"""
                if fv.surface_libre > A.surface_libre and fv.surface_libre > B.surface_libre:
                    nouveaux.append(fv)
                    utilises[i]=True
                    utilises[j]=True
                    break
 
            # Fusion horizontale : chevauchement en y, un rectangle avec un plus grand x est cree
            y_bas = max(A.get_y(), B.get_y())
            y_haut = min(A.get_y() + A.get_ly(), B.get_y() + B.get_ly())
            if y_haut - y_bas > 0:
                x_gauche = min(A.get_x(), B.get_x())
                x_droit = max(A.get_x() + A.get_lx(), B.get_x() + B.get_lx())
                fh = EspaceLibre(x_gauche, y_bas,
                                 x_droit - x_gauche, y_haut - y_bas)"""fh =fusion horizontale"""
                if fh.surface_libre > A.surface_libre and fh.surface_libre > B.surface_libre:
                    nouveaux.append(fh)
                    utilises.add(i); utilises.add(j)
                    break
 
    if not nouveaux:
        return espaces
 
    result = [espaces[k] for k in range(len(espaces)) if k not in utilises]
    result.extend(nouveaux)
    result.sort(key=lambda e: e.surface_libre, reverse=True)
    return result
    
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

        # 1. Chercher la meilleure tôle déjà utilisée
    meilleur_score = -1
    resultat = None
    tole_idx = None
    indice_tole = 0
    
    for espaces in plans_espaces:    
        res = _meilleur_placement(espaces, figure, autoriser_rotation)
    
        if res is not None:    
            surface_tole = tole.get_x() * tole.get_y()    
            surface_utilisee = 0
            for p in solution.plans[indice_tole].placements:
                surface_utilisee += p.figure.get_x() * p.figure.get_y()    
            surface_figure = res[1] * res[2]    
            score = (surface_utilisee + surface_figure) / surface_tole    
            if score > meilleur_score:
                meilleur_score = score
                resultat = res
                tole_idx = indice_tole
    
        indice_tole += 1
    
    
    # 2. Si aucune tôle ne marche → essayer de fusionner
    if resultat is None:    
        indice_tole = 0    
        for espaces in plans_espaces:    
            espaces_fusionnes = _fusionner_espaces(espaces)    
            res = _meilleur_placement(espaces_fusionnes, figure, autoriser_rotation)
    
            if res is not None:
                plans_espaces[indice_tole] = espaces_fusionnes
                resultat = res
                tole_idx = indice_tole
                break    
            indice_tole += 1
    
    
    # 3. Si toujours rien → créer une nouvelle tôle
    if resultat is None:    
        tole_idx = len(solution.plans)    
        espace_initial = EspaceLibre(0, 0, tole.get_x(), tole.get_y())    
        plans_espaces.append([espace_initial])
        solution.plans.append(TolePlan(tole))
    
        resultat = _meilleur_placement(plans_espaces[tole_idx],figure,autoriser_rotation)
    
        if resultat is None:
            raise ValueError("Figure trop grande pour la tôle")    
    
    # 4. Placer la figure
    indice_espace, largeur, hauteur = resultat    
    espace = plans_espaces[tole_idx][indice_espace]    
    tournee = (largeur != figure.get_x())
    
    solution.plans[tole_idx].placements.append(Placement(figure, espace.get_x(), espace.get_y(), tournee))
    
    
    # 5. Découper l’espace
    nouveaux_espaces = _decouper_guillotine(espace, figure, tournee)    
    plans_espaces[tole_idx].pop(indice_espace)
    
    for e in nouveaux_espaces:
        plans_espaces[tole_idx].append(e)    
    plans_espaces[tole_idx].sort(key=lambda esp: esp.surface_libre,reverse=True)
    return solution    
