import Fonderie
import Plaques

def triviale(fonderie : Fonderie, plaques : Plaques):

    nb_plaques = 0
    for _ in plaques.get_list_f():
        nb_plaques += 1
    
    tole = fonderie.get_tole()[0]
    volume_tole = tole.get_x() * tole.get_y() * tole.get_z()
    volume_total = nb_plaques * volume_tole
    
    cout_fonte = volume_total * fonderie.get_cout()

    cout_metaux = 0
  
    cout_total = cout_metaux + cout_fonte
    
    return nb_plaques, cout_total

def triviale2(fonderie : Fonderie, plaques : Plaques):
    nombre_plaques = len(plaques.get_liste_f())
    '''on compare les alliages présents en stock pour trouver le moins cher à produire'''
    liste_achat1 = []
    liste_prix_achats = []
    for alliage in fonderie.get_liste_all():
        for i in range(len(alliage.get_list_pct())):
            epsilon1 = alliage.get_list_pct[i] - fonderie.get_client().get_pct_min()[i]
            epsilon2 = alliage.get_list_pct[i] - fonderie.get_client().get_pct_max()[i]
            '''on compare les pct des différents métaux aux pct min et max voulus par le client pour déterminer les métaux à acheter'''
            if epsilon1 > 0 and epsilon2 < 0 :
                liste_achat1.append(0)
            elif epsilon1 > 0:
                liste_achat1.append(alliage.get_list_prix[i] * epsilon1)
            elif epsilon2 < 0:
                liste_achat1.append(alliage.get_list_prix[i] * epsilon2)
            count = 0
            for _ in liste_achat1 :
                count +=1
            liste_prix_achats.append(count)

def triviale3(fonderie : Fonderie, plaques : Plaques):
    nombre_plaques = len(plaques.get_liste_f())
    volume_plaque = fonderie.get_list_tole()[0].get_x() * fonderie.get_list_tole()[0].get_y() * fonderie.get_list_tole()[0].get_z()
    liste_prix = []
    liste_solution = []
    for j in range(len(fonderie.get_list_all())):
        '''on boucle sur le nombre d'alliages'''
        prix_achat = 0
        liste_achats = []

        for i in range(len(fonderie.get_liste_all()[j].get_liste_pct())):
            '''on récupère le prix d'achat de chaque métal en choisissant l'alliage j'''
            pct_moyen = (fonderie.get_client().get_pct_max()[i] + fonderie.get_client().get_pct_min()[i]) / 2
            masse_requise = nombre_plaques * fonderie.get_liste_all()[i].get_liste_mv()[i] * pct_moyen * volume_plaque
            masse_possedee = fonderie.get_list_kg()[j] * fonderie.get_list_all()[j].get_list_pct()[i]
            masse_achat = masse_requise - masse_possedee
            if masse_achat <=0:
                masse_achat = 0
                          
            liste_achats.append(masse_achat)
            prix_achat += masse_achat * fonderie.get_list_prix()[i]
        
        liste_prix.append(prix_achat)

"""
Exemple de programme permettant de résoudre le problème du Jardin vu en cours
max   4 xC + 5 xN
s.t.  2 xC + 1 xN <= 8
      1 xC + 2 xN <= 7
      0 xC + 1 xN <= 3
        xC ,   xN >= 0
"""

"""
Pour la fonderie on veut résoudre :
min sum(i for i in range(len(fonderie.get_list_prix()[i]))(m[i] * fonderie.get_list_prix()[i])
"""
from math import inf
from typing import List, Tuple
import pulp


def resoudre_fonderie(rendements: List[float], stocks: List[float], conso: List[List[float]]) \
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


'''
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
'''

def test_fonderie(fonderie, plaques):
    return fonderie.get_list_all()[0].get_kg()