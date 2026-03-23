import Client
import Fonderie
import Alliage
import Tole
import Fournisseur
import Plaque
import Polygone

def read_file(file):
    f= open(file, "r")
    with f:
        if file.find("_fonderie") >= 0:
            r = f.readlines()
            '''on crée les deux alliages possibles'''
            i_pkg = r[2]
            i_pkg.strip()
            i_pkg.split()

            i_mv = r[3]
            i_mv.strip()
            i_mv.split()

            i_pct1 = r[6]
            i_pct1.strip()
            i_pct1.split()
            kg1 = i_pct1[:1]
            i_pct1 = i_pct1[1:]

            i_pct2 = r[7]
            i_pct2.strip()
            i_pct2.split()
            kg2 = i_pct2[:1]
            i_pct2 = i_pct2[1:]

            all1 = Alliage.Alliage(i_mv, i_pkg, i_pct1)
            all2 = Alliage.Alliage(i_mv, i_pkg, i_pct2)

            '''on crée les deux toles possibles'''
            i_tole = r[0]
            i_tole.strip()
            i_tole.split()
            tole1 = Tole.Tole(i_tole[0], i_tole[1], i_tole[2], all1)
            tole2 = Tole.Tole(i_tole[0], i_tole[1], i_tole[2], all2)

            '''on crée le client'''
            i_pmin = r[4]
            i_pmin.strip()
            i_pmin.split()

            i_pmax = r[5]
            i_pmax.strip()
            i_pmax.split()

            client = Client.Client(i_pmax, i_pmin)

            i_cout = r[1]

            '''on crée la fonderie'''
            list_tole = [tole1, tole2]
            list_all = [all1, all2]
            list_p = [kg1, kg2]
            fonderie = Fonderie.Fonderie(list_tole, list_all, client, list_p, i_cout)


        elif file.find("_fournisseurs") >= 0:
            r = f.readlines()
            '''on crée un dictionnaire de fournisseurs'''
            d_fournisseurs : dict[Fournisseur] = {}
            for i in range(len(r)):
                i_fi = r[i]
                i_fi.strip()
                i_fi.split()
                d_fournisseurs[i_fi[0]] = Fournisseur.Fournisseur(i_fi[1], i_fi[2], i_fi[3])

        elif file.find("_plaque") >= 0:
            r = f.readlines()
            i_prix = r[0]
            i_prix.strip()
            i_prix.split()
            '''on crée le dictionnaire des figures à découper'''
            d_plaques : dict[Polygones] = {}
            for i in range(1,len(r)):
                i_pi = r[i]
                i_pi.strip()
                i_pi.split()
                d_plaques[i_pi[0]] = Polygone.Polygone(i_pi[1], i_pi[2], i_pi[3])

            plaque = Plaque.Plaque(i_prix[0], d_plaques)

        else:
            raise(ValueError)


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
    # TODO
    duree: float = time.time() - debut
    print(f"Durée d'execution : {round(100 * duree) / 100} secondes")


if __name__ == "__main__":
    read_file("instances\InstB_fonderie.txt")

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