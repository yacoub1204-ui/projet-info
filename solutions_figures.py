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
