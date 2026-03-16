import client
import fonderie
import main
import materiau
import tole

def read_file(file : str):
    if file.find("_fonderie") >= 0:

    elif file.find("_fournisseurs") >= 0:

    elif file.find("_plaque") >= 0:

    else:
        raise(ValueError)


"""
Fichier à completer
Seule la méthode resoudre() sera appelee
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
    # TODO
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
    
        
