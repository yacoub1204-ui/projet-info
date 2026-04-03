import Figure
from Point import Point
import Polygone

def triviale(figure : Figure):
    '''triviale : on parcourt la figure en prenant le premier point de chaque polygone'''
    solution : list[Point] = []
    for i in range(len(figure.get_list_poly())):
        solution.append(i)
        solution.append(0)
    return solution
def diagonalmax(figure):
    '''diagonalmax : on parcourt les polygones dans l'ordre de leur point 
    le plus proche de la diagonale (0,0) -> point le plus éloigné'''
    
    # 1. Trouver le point le plus éloigné de l'origine dans toute la figure
    point_loin = None
    distance_max = 0
    origine = Point(0, 0)
    
    for polygone in figure.get_list_poly():
        for point in polygone.get_list_points():
            dist = origine.distance(point)
            if dist > distance_max:
                distance_max = dist
                point_loin = point
    
    # 2. Pour chaque polygone, trouver l'index du point le plus proche de la diagonale
    points_diagonale = []
    
    liste_poly = figure.get_list_poly()
    for i in range(len(liste_poly)):
        polygone = liste_poly[i]
        point = polygone.point_plus_proche_droite(origine, point_loin)  # Corrigé ici
        # Trouver l'index de ce point dans le polygone
        index_point = polygone.get_list_points().index(point)
        points_diagonale.append((i, index_point, point))
    
    # 3. Trier les polygones par distance depuis (0,0)
    points_diagonale.sort(key=lambda x: origine.distance(x[2]))
    
    # 4. Construire la solution au format attendu
    solution = []
    for index_poly, index_point, _ in points_diagonale:
        solution.append(index_poly)
        solution.append(index_point)
    
    return solution
def glouton(figure, point_depart=None):
    if point_depart is None:
        point_depart = Point(0, 0) 
    polygones_restants = figure.get_list_poly()[:]
    solution = [point_depart]
    point_actuel = point_depart
    
    while polygones_restants:
        meilleur_point = None
        meilleure_distance = 99999
        meilleur_polygone = None
        
        for polygone in polygones_restants:
            for point in polygone.get_list_points():
                distance_actuel = point_actuel.distance(point)
                if distance_actuel < meilleure_distance:
                    meilleure_distance = distance_actuel
                    meilleur_point = point
                    meilleur_polygone = polygone
        
        
        index_poly = figure.get_list_poly().index(meilleur_polygone)
        solution.append(index_poly)  
        solution.append(meilleur_point)
        point_actuel = meilleur_point
        polygones_restants.remove(meilleur_polygone)
        
    return solution




import time
import copy

def beam_search(figure, nbrdeconcurent=2, limite=10):
    depart = time.time()
    point_depart = Point(0, 0)
    polygones = figure.get_list_poly()
    nb_poly = len(polygones)
    
    # le chemin = (points, position, indices_points, longueur, visites)
    chemins = [([point_depart], [], [], 0.0, [])]
    meilleure_solution = None
    meilleur_long = 99999 #pour la mettre a l'infini
    
    while (time.time() - depart) < limite: # on cree un nouveaux chemin jusqua qu'on a depassé la limite
        nouveaux_chemins = []
        for points, position, reelindicedupoint, long, visites in chemins:
            dernier_point = points[-1]
            restants = []
            for i in range(len(polygones)):
                if i not in visites:
                    restants.append(polygones[i])   #on cherche les points qu'on a pas visité
            
            if not restants:                # lorsquon a plus de valeur on classe la meilleur valeur au dessus 
                if long < meilleur_long:
                    meilleur_long = long
                    meilleure_solution = (points, position, reelindicedupoint)
                continue
            
            for poly in restants:           #pour les valeurs pas visité on crée des noouveau chemin jusqua ne plus avoir ne chemin 
                for point in poly.get_list_points():
                    distance = dernier_point.distance(point)
                    idice_polygone = polygones.index(poly)
                    idice_point = poly.get_list_points().index(point)
                    nouveau_points = points + [point]
                    nouvelle_position = position + [idice_polygone]
                    nouveaux_indices = reelindicedupoint + [idice_point]
                    nouvolong = long + distance
                    nouveaux_visites = visites + [idice_polygone]

                    nouveaux_chemins.append((nouveau_points, nouvelle_position, nouveaux_indices, nouvolong, nouveaux_visites))
        if not nouveaux_chemins:            # quand on a plus de chemin cest qu'on a tous visité 
            break
        nouveaux_chemins.sort(key=lambda x: x[3])           #on classe par rapport a leur longueur
        chemins = nouveaux_chemins[:nbrdeconcurent]         #les valeur du chemin cest les valeur quon a cho
    
    if meilleure_solution:
        point, nums, idice_point = meilleure_solution
        solution = []
        for i in range(len(nums)):
            solution.append(nums[i])
            solution.append(idice_point[i])  # indice du point (entier)
        return solution
    else:
        return glouton(figure, point_depart)  #Si aucune solution est trouvé dans le temps impartie on fait un algo glouton
