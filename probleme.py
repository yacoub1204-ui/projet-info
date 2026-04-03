import Printer
import reader2
import solutions_figures
import solutions_fournisseurs
import solution_decoupe_2
"""
Fichier à completer
Seule la méthode resoudre() sera appelée
"""
import os
import time


def resoudre(inst: str):
   
    debut: float = time.time()

    # on récupère les données de l'instance choisie grâce au reader
    data = reader2.read(inst)       # CORRIGE : read() appelé une seule fois et stocké

    fonderie = data["fonderie"]
    plaques  = data["plaques"]

    # on peut écrire la solution grâce au printer
    solution = Printer.Printer(fonderie, plaques)
    with open(f"{inst}_sol.txt", "w") as file:
        file.write(solution.print_fournisseurs(solutions_fournisseurs.test_fonderie))
        file.write(solution.print_figures(solutions_figures.triviale))
        file.write(solution.print_paques(solution_decoupe_2.decouper))

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
