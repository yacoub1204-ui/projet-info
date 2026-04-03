import Figure
import Point

def triviale(figure : Figure):
    '''triviale : on parcourt la figure en prenant le premier point de chaque polygone'''
    solution : list[Point] = []
    for i in range(len(figure.get_list_poly())):
        solution.append(i)
        solution.append(0)
    return solution

def diagonalmax(plaques):
    pointsolus = []
    solution = []
    for polygone in plaques.get_list_polygone():
        pointsolus.append(polygone.point_plus_proche_droite((0, 0), figure.point_plus_loin()))

    pointactuel = Point(0, 0)

    while pointsolus:  
        solution.append(pointactuel)
        pointactuel = pointactuel.point_proche_liste(pointsolus)
        pointsolus.remove(pointactuel)

    return solution