import Printer

import reader2
from solution_decoupe_2 import decoupe
import solutions_figures
import solutions_fournisseurs
import TolePlan
"""
Fichier à completer
Seule la méthode resoudre() sera appelée
"""
import os
import time


def resoudre(inst: str):
    """
    Cette methode est la seule qui sera appelee par le checker

    :param inst: nom de l'instance traitee
    :return: rien
    """
    debut: float = time.time()

    '''on récupère les données de l'instance choisie grâce au reader'''
    print(reader2.read(inst))

    fonderie = reader2.read(inst)["fonderie"]
    plaques = reader2.read(inst)["plaques"]

    '''on peut écrire la solution grâce au printer'''

    solution = Printer.Printer(fonderie, plaques)
    with open(f"{inst}_sol.txt", "w") as file:
        file.write(solution.print_fournisseurs(solutions_fournisseurs.fonderie_pl))
        solution_decoupe = decouper(tole, plaques)
        file.write(solution_decoupe.nb_toles())#=nbr toles utiliseees
        file.write(solution.print_figures(solutions_figures.triviale))
        solution_decoupe = decouper(tole, plaques)
        file.write(solution_decoupe.nb_toles())#=nbr toles utiliseees
        

        for i, plan in enumerate(self._plans):
            print(f"\n--- Tôle {i+1} ---")
            for p in plan.get_placements():
                print(p)
    duree: float = time.time() - debut
    print(f"Durée d'execution : {round(100 * duree) / 100} secondes")


if __name__ == "__main__":
    
    instance = "nom_instance"
    time_max = 60
    if os.path.exists("CONFIG"):
        with open("CONFIG", "r") as fichier_config:
            for ligne in fichier_config.readlines():
                if '=' not in ligne:
                    continue
                mots = [_.strip() for _ in ligne.split("=")]
                if mots[0].upper() == "INSTANCE":
                    instance = mots[1]
    resoudre(instance)
