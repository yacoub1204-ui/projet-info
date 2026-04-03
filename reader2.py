import Client
import Fonderie2
import Alliage2
import Tole
import Fournisseur
import Plaques
import Polygone
import Point
import Figure
import Materiau
 
def read(instance):
 
    list_files = []
    list_files.append(f"{instance}_fonderie.txt")
    list_files.append(f"{instance}_fournisseurs.txt")
    list_files.append(f"{instance}_plaques.txt")
 
    # dictionnaire des donnees
    data_dict = {}
 
    # dictionnaire des figures a decouper
    dictionnaire_figures = {}
 
    for element in list_files:
        f = open(element, "r")
        with f:
 
            if element.find(f"{instance}_fonderie.txt") >= 0:
                r = f.readlines()
 
                # dimensions des toles et cout de fonte
                ligne = r[0].strip().split()
                x = float(ligne[0])
                y = float(ligne[1])
                z = float(ligne[2])
 
                cout = float(r[1].strip())
 
                # on cree les materiaux du probleme
                prix_kg = r[2].strip().split()
                mv = r[3].strip().split()
 
                liste_materiau : list[Materiau.Materiau] = []
                for i in range(len(mv)):
                    m = Materiau.Materiau(float(mv[i]), float(prix_kg[i]))
                    liste_materiau.append(m)
 
                # pourcentages min et max demandes par le client
                pct_min = [float(pct) for pct in r[4].strip().split()]
                pct_max = [float(pct) for pct in r[5].strip().split()]
                client = Client.Client(pct_max, pct_min)
 
                # liste des alliages en stock
                liste_stock : list[Alliage2.Alliage2] = []
                for i in range(6, len(r)):
                    ligne_alliage = r[i].strip().split()
                    if len(ligne_alliage) == 0:
                        continue
                    poids = float(ligne_alliage[0])
                    pct = [float(v) for v in ligne_alliage[1:]]
                    liste_stock.append(Alliage2.Alliage2(poids, pct))
 
                # on cree la tole que la fonderie peut produire
                tole = Tole.Tole(x, y, z)
 
                # on cree la fonderie
                data_dict["fonderie"] = Fonderie2.Fonderie2(tole, liste_materiau, liste_stock, client, cout)
 
            elif element.find(f"{instance}_fournisseurs.txt") >= 0:
                r = f.readlines()
 
                # on cree une liste de fournisseurs
                liste_fournisseurs : list[Fournisseur.Fournisseur] = []
                for i in range(len(r)):
                    fournisseur = r[i].strip().split()
                    if len(fournisseur) >= 4:
                        liste_fournisseurs.append(Fournisseur.Fournisseur(fournisseur[1], fournisseur[2], fournisseur[3]))
 
                data_dict["fournisseurs"] = liste_fournisseurs
 
            elif element.find(f"{instance}_plaques.txt") >= 0:
                r = f.readlines()
 
                # cout du deplacement laser sans perforation
                prix = r[0].strip().split()
 
                # dictionnaire dont la clé est le nom de la figure et la valeur le nombre d'exemplaire a produire
                noms_figures : list[str] = []
                for i in range(1, len(r)):
                    ligne = r[i].strip().split()
                    if len(ligne) >= 2:
                        nom_figure = ligne[0]
                        nombre = int(ligne[1])
                        noms_figures.append(nom_figure)
                        # cle : nom de la figure, valeur : quantite commandee
                        dictionnaire_figures[nom_figure] = nombre
 
                # lecture des fichiers de description de chaque modele de plaque
                # dictionnaire temporaire nom_figure -> objet Figure
                modeles : dict[str, Figure.Figure] = {}
                for nom_figure in noms_figures:
                    l = open(f"{instance}_{nom_figure}.txt", "r")
                    with l:
                        e = l.readlines()
 
                        # dimensions de la plaque
                        dimensions = e[0].strip().split()
                        fx = float(dimensions[0])
                        fy = float(dimensions[1])
 
                        # lecture des polygones
                        liste_polygones : list[Polygone] = []
                        for i in range(1, len(e)):
                            polygone = e[i].strip().split()
                            liste_points : list[Point.Point] = []
                            if len(polygone) != 0:
                                for j in range(0, len(polygone), 2):
                                    if j + 1 < len(polygone):
                                        x = polygone[j]
                                        y = polygone[j + 1]
                                        point = Point.Point(int(float(x)), int(float(y)))
                                        liste_points.append(point)
                                p = Polygone.Polygone(liste_points)
                                liste_polygones.append(p)
 
                        modeles[nom_figure] = Figure.Figure(nom_figure, fx, fy, liste_polygones)
 
                # liste_figures : un objet Figure par exemplaire commande
                liste_figures : list[Figure.Figure] = []
                for nom_figure in noms_figures:
                    for j in range(dictionnaire_figures[nom_figure]):
                        liste_figures.append(modeles[nom_figure])
 
                data_dict["plaques"] = Plaques.Plaques(prix, liste_figures, 0)
 
            else:
                continue
 
    return data_dict