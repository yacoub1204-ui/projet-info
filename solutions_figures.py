from __future__ import annotations
import Figure
import Point

def triviale(figure : Figure.Figure):
    '''triviale : on parcourt la figure en prenant le premier point de chaque polygone'''
    solution : list[Point.Point] = []
    for polygone in figure.get_list_poly():
        solution.append(polygone.get_list_points()[0])  # CORRIGE : get_list_points() ajouté dans Polygone
    return solution

def diagonalmax(figure : Figure.Figure):   # CORRIGE : paramètre renommé figure (était plaques, incohérent)
    pointsolus = []
    solution = []
    for polygone in figure.get_list_poly():     # CORRIGE : get_list_poly() au lieu de get_list_polygone()
        pointsolus.append(polygone.point_plus_proche_droite((0, 0), figure.get_list_poly()[-1].get_list_points()[-1]))

    pointactuel = Point.Point(0, 0)             # CORRIGE : Point.Point() au lieu de Point()

    while pointsolus:
        solution.append(pointactuel)
        pointactuel = pointactuel.point_proche_liste(pointsolus)
        pointsolus.remove(pointactuel)

    return solution

def glouton(figure, point_depart=None):
    if point_depart is None:
        point_depart = Point(0, 0) 
    polygones_restants = figure.get_list_poly()[:]
    solution = [point_depart]
    point_actuel = point_depart
    
    while polygones_restants:
        meilleur_point = None
        meilleure_distance = float('inf')
        meilleur_polygone = None
        
        for polygone in polygones_restants:
            for point in polygone.get_list_points():
                distance_actuel = point_actuel.distance(point)
                if distance_actuel < meilleure_distance:
                    meilleure_distance = distance_actuel
                    meilleur_point = point
                    meilleur_polygone = polygone
        
        # Trouver l'INDEX du polygone (pas un compteur)
        index_poly = figure.get_list_poly().index(meilleur_polygone)
        solution.append(index_poly)  # ← utilise index, pas numero
        solution.append(meilleur_point)
        point_actuel = meilleur_point
        polygones_restants.remove(meilleur_polygone)
        
    return solution
import time
import copy

import time
from copy import deepcopy
def beam_search(figure, beam_width=3, timeout=40):
    depart = time.time()
    point_depart = Point(0, 0)
    polygones = figure.get_list_poly()
    nb_poly = len(polygones)
    
    # (points, nums, indices_points, cout, visites)
    chemins = [([point_depart], [], [], 0.0, set())]
    meilleure_solution = None
    meilleur_cout = float('inf')
    
    while (time.time() - depart) < timeout:
        nouveaux_chemins = []
        for points, nums, idx_pts, cout, visites in chemins:
            dernier_point = points[-1]
            restants = [p for i, p in enumerate(polygones) if i not in visites]
            
            if not restants:
                if cout < meilleur_cout:
                    meilleur_cout = cout
                    meilleure_solution = (points, nums, idx_pts)
                continue
            
            for poly in restants:
                for point in poly.get_list_points():
                    dist = dernier_point.distance(point)
                    idx_poly = polygones.index(poly)
                    idx_point = poly.get_list_points().index(point)
                    nouveaux_chemins.append((
                        points + [point],
                        nums + [idx_poly],
                        idx_pts + [idx_point],
                        cout + dist,
                        visites | {idx_poly}
                    ))
        
        if not nouveaux_chemins:
            break
        nouveaux_chemins.sort(key=lambda x: x[3])
        chemins = nouveaux_chemins[:beam_width]
    
    if meilleure_solution:
        points, nums, idx_pts = meilleure_solution
        resultat = []
        for i in range(len(nums)):
            resultat.append(nums[i])
            resultat.append(idx_pts[i])  # indice du point (entier)
        return resultat
    else:
        return glouton(figure, point_depart)  # mais glouton aussi doit être modifié
