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
    
    for i, polygone in enumerate(figure.get_list_poly()):
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
def solution_gloutonne(figure, point_depart=None):
    """Solution gloutonne : toujours prendre le point le plus proche du point courant"""
    if point_depart is None:
        point_depart = Point(0, 0) 
    polygones_restants = figure.get_list_poly()[:]
    solution = [point_depart]
    point_actuel = point_depart
    numero =0
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
        numero +=1
        solution.append(numero)
        solution.append(meilleur_point)
        point_actuel = meilleur_point
        polygones_restants.remove(meilleur_polygone)
        
    return solution
def beam_search(figure, beam_width=3, depth=5, iterations=10):
    """Recherche beam search pour trouver le trajet optimal à travers les polygones
    
    Args:
        figure: Figure contenant les polygones à visiter
        beam_width: nombre de meilleurs candidats à garder à chaque niveau
        depth: profondeur de recherche (nombre de polygones à explorer en profondeur)
        iterations: nombre de redémarrages pour éviter les optimums locaux
    
    Returns:
        liste alternant [index_polygone, index_point, ...] compatible avec triviale
    """
    
    point_depart = Point(0, 0)
    
    # Obtenir le meilleur trajet (liste de points)
    trajet_glouton = solution_gloutonne(figure, point_depart)
    meilleur_trajet = trajet_glouton
    meilleure_longueur = longueur_trajet(trajet_glouton)
    
    for i in range(iterations):
        trajet_candidat = beam_search_iteration(figure, point_depart, beam_width, depth)
        longueur_candidat = longueur_trajet(trajet_candidat)
        
        if longueur_candidat < meilleure_longueur:
            meilleur_trajet = trajet_candidat
            meilleure_longueur = longueur_candidat
    
    # Convertir le trajet (liste de points) en solution (liste d'indices)
    solution = []
    
    # Ignorer le point de départ (0,0) qui est le premier élément
    for point in meilleur_trajet[1:]:
        # Trouver dans quel polygone se trouve ce point
        for i, polygone in enumerate(figure.get_list_poly()):
            if point in polygone.get_list_points():
                index_point = polygone.get_list_points().index(point)
                solution.append(i)
                solution.append(index_point)
                break
    
    return solution
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
    
    for i, polygone in enumerate(figure.get_list_poly()):
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
