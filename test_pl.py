"""
Exemple de programme permettant de résoudre le problème du Jardin vu en cours
max   4 xC + 5 xN
s.t.  2 xC + 1 xN <= 8
      1 xC + 2 xN <= 7
      0 xC + 1 xN <= 3
        xC ,   xN >= 0
"""
from math import inf
from typing import List, Tuple
import pulp


def resoudre_jardin(rendements: List[float], stocks: List[float], conso: List[List[float]]) \
        -> Tuple[float, List[float], List[float]]:
    """
    Résolution du problème du jardin
    :param rendements: rendement[i] est le rendement du légume i
    :param stocks: stocks[j] est la quantité disponible de la ressource j
    :param conso: conso[i][j] est la consommation unitaire du légume j en ressource i
    :return: la valeur optimale de l'objectif, la solution optimale primale, la solution optimale duale
    """
    # Données des ensembles pour simplifier l'écriture
    nb_legumes: int = len(rendements)
    nb_ressources: int = len(stocks)
    legumes = range(nb_legumes)
    ressources = range(nb_ressources)

    # Modèle
    modele: pulp.LpProblem = pulp.LpProblem("Jardin", pulp.LpMaximize)

    # Variables de décision
    superficie: List[pulp.LpVariable] = \
        [pulp.LpVariable(f"superficie_{leg}", lowBound=0, cat="Continuous") for leg in legumes]

    # Fonction objectif
    modele += pulp.lpSum(rendements[leg] * superficie[leg] for leg in legumes)

    # Contraintes
    cont_stock: List[pulp.LpConstraint] = \
        [pulp.lpSum(conso[res][leg] * superficie[leg] for leg in legumes) <= stocks[res] for res in ressources]
    for res in ressources:
        modele += cont_stock[res], f"respect_stock_{res}"

    # Résolution (en demandant de supprimer les messages pulp)
    modele.solve(pulp.PULP_CBC_CMD(msg=False))

    # Definition des valeurs renvoyées
    print("Statut de la résolution:", pulp.LpStatus[modele.status])
    if modele.status == pulp.constants.LpSolutionOptimal:
        # si la résolution a réussi on renvoie la valeur de l'objectif, et des solutions primales et duales
        return pulp.value(modele.objective), \
               [superficie[leg].varValue for leg in legumes], \
               [cont_stock[res].pi for res in ressources]
    else:
        # si le statut n'est pas Optimal c'est qu'il y a eu un problème (PL non réalisable ou non borné)
        return -inf, [], []


if __name__ == "__main__":
    # Données
    rendements: List[float] = [4, 5]
    stocks: List[float] = [8, 7, 3]
    conso: List[List[float]] = [
        [2, 1],
        [1, 2],
        [0, 1]
    ]
    # Résolution avec en retour les valeurs de l'objectif, et des solutions optimales primale et duale
    objectif, x, y = resoudre_jardin(rendements, stocks, conso)
    print("Objectif :", objectif)
    print("Solution primale:", x)
    print("Solution duale:", y)