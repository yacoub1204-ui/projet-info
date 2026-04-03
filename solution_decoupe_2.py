


class Placement:
    def __init__(self, figure, x_origine, y_origine, tournee):
        self._figure = figure
        self._x = x_origine
        self._y = y_origine
        self._tournee = tournee

    def get_figure(self):
        return self._figure

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_tournee(self):
        return self._tournee


class Figure:
    def __init__(self, nom, x, y, list_poly, r=0):
        self._nom = nom
        self._x = x
        self._y = y
        self._list_poly = list_poly
        self._r = r

    def get_nom(self):
        return self._nom

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_list_poly(self):
        return self._list_poly


class Tole:
    def __init__(self, x, y):
        self._tole_x = x
        self._tole_y = y

    def get_x(self):
        return self._tole_x

    def get_y(self):
        return self._tole_y


class TolePlan:
    def __init__(self, tole):
        self._tole = tole
        self._placements = []

    def get_tole(self):
        return self._tole

    def get_placements(self):
        return self._placements


class EspaceLibre:
    def __init__(self, x, y, lx, ly):
        self._x = x
        self._y = y
        self._lx = lx
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

    def rentre_dedans(self, largeur, hauteur):
        return largeur <= self._lx and hauteur <= self._ly

    def gaspillage(self, largeur, hauteur):
        return self.surface_libre() - largeur * hauteur  


# Algo decoupe
def _decouper_guillotine(espace, figure, tournee):
    # decoupe un espace libre apres le placement d'un rectangle
    reste = []
    if tournee:
        fx = figure.get_y()     # largeur figure/plaque placee
        fy = figure.get_x()
    else:
        fx = figure.get_x()
        fy = figure.get_y()

    r_x = espace.get_lx() - fx     # reste en x
    r_y = espace.get_ly() - fy

    if r_x >= r_y:      # coupe horizontale -> grand espace en haut
        if r_y > 0:
            reste.append(EspaceLibre(espace.get_x(), espace.get_y() + fy, espace.get_lx(), r_y))  
        if r_x > 0:
            reste.append(EspaceLibre(espace.get_x() + fx, espace.get_y(), r_x, fy))
    else:               # coupe verticale -> grand espace a droite
        if r_x > 0:
            reste.append(EspaceLibre(espace.get_x() + fx, espace.get_y(), r_x, espace.get_ly()))
        if r_y > 0:
            reste.append(EspaceLibre(espace.get_x(), espace.get_y() + fy, fx, r_y))

    resultat = []
    for e in reste:
        if e.surface_libre() > 0:
            resultat.append(e)

    return resultat


def _fusionner_espaces(espaces):
    """Tente de fusionner des paires d'espaces dont les intervalles x ou y
    se chevauchent pour créer un rectangle d'espace libre qui traverse les autres."""
    if len(espaces) < 2:
        return espaces

    utilises = [0] * len(espaces)
    nouveaux = []

    for i in range(len(espaces)):
        if utilises[i]!=0:
            continue
        for j in range(i + 1, len(espaces)):
            if utilises[j]==1:
                continue

            A = espaces[i]
            B = espaces[j]

            # Fusion verticale : chevauchement en x
            x_gauche = max(A.get_x(), B.get_x())
            x_droit = min(A.get_x() + A.get_lx(), B.get_x() + B.get_lx())
            if x_droit - x_gauche > 0:
                y_bas = min(A.get_y(), B.get_y())
                y_haut = max(A.get_y() + A.get_ly(), B.get_y() + B.get_ly())
                fv = EspaceLibre(x_gauche, y_bas, x_droit - x_gauche, y_haut - y_bas)
                if fv.surface_libre() > A.surface_libre() and fv.surface_libre() > B.surface_libre():
                    nouveaux.append(fv)
                    utilises[i] = 1
                    utilises[j] =1
                    break

            # Fusion horizontale : chevauchement en y
            y_bas = max(A.get_y(), B.get_y())
            y_haut = min(A.get_y() + A.get_ly(), B.get_y() + B.get_ly())
            if y_haut - y_bas > 0:
                x_gauche = min(A.get_x(), B.get_x())
                x_droit = max(A.get_x() + A.get_lx(), B.get_x() + B.get_lx())
                fh = EspaceLibre(x_gauche, y_bas, x_droit - x_gauche, y_haut - y_bas)
                if fh.surface_libre() > A.surface_libre() and fh.surface_libre() > B.surface_libre():
                    nouveaux.append(fh)
                    utilises[i] = 1
                    utilises[j] = 1
                    break

    if not nouveaux:
        return espaces

    result = [espaces[k] for k in range(len(espaces)) if not utilises[k]]
    result.extend(nouveaux)
    result.sort(key=lambda e: e.surface_libre(), reverse=True)
    return result


def _meilleur_placement(espaces, figure, autoriser_rotation):
    meilleur = None
    meilleur_gasp = float('inf')
    fx = figure.get_x()
    fy = figure.get_y()
    orientations = [(fx, fy)]
    if autoriser_rotation and fx != fy:
        orientations.append((fy, fx))

    indice = 0
    for espace in espaces:
        for orientation in orientations:
            largeur = orientation[0]
            hauteur = orientation[1]
            if espace.rentre_dedans(largeur, hauteur):   
                gaspillage = espace.gaspillage(largeur, hauteur)
                if gaspillage < meilleur_gasp:
                    meilleur = (indice, largeur, hauteur)
                    meilleur_gasp = gaspillage  
        indice += 1

    return meilleur


# Algo principal
def decouper(tole, plaques):
    autoriser_rotation = True
    figures = sorted(plaques.get_list_f(), key=lambda f: f.get_x() * f.get_y(), reverse=True)

    tole_plans = []
    plans_espaces = []

    for figure in figures:
        meilleur_score = -1
        resultat = None
        tole_idx = None
        indice_tole = 0

        # 1. Chercher la meilleure tôle déjà utilisée
        for espaces in plans_espaces:
            res = _meilleur_placement(espaces, figure, autoriser_rotation)
            if res is not None:
                surface_tole = tole.get_x() * tole.get_y()
                surface_utilisee = 0
                for p in tole_plans[indice_tole].get_placements():   
                    f = p.get_figure()
                    if p.get_tournee():
                        surface_utilisee += f.get_y() * f.get_x()
                    else:
                        surface_utilisee += f.get_x() * f.get_y()    
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
            tole_idx = len(tole_plans)    
            espace_initial = EspaceLibre(0, 0, tole.get_x(), tole.get_y())
            plans_espaces.append([espace_initial])
            tole_plans.append(TolePlan(tole))    
            resultat = _meilleur_placement(plans_espaces[tole_idx], figure, autoriser_rotation)
            if resultat is None:
                raise ValueError("Figure trop grande pour la tole")

        # 4. Placer la figure
        indice_espace, largeur, hauteur = resultat
        espace = plans_espaces[tole_idx][indice_espace]
        tournee = (largeur != figure.get_x())
        tole_plans[tole_idx].get_placements().append(   
            Placement(figure, espace.get_x(), espace.get_y(), tournee)
        )

        # 5. Découper l'espace
        nouveaux_espaces = _decouper_guillotine(espace, figure, tournee)
        plans_espaces[tole_idx].pop(indice_espace)
        for e in nouveaux_espaces:
            plans_espaces[tole_idx].append(e)
        plans_espaces[tole_idx].sort(key=lambda e: e.surface_libre(), reverse=True)    

    return tole_plans


