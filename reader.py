import Client
import Fonderie
import Alliage
import Tole
import Fournisseur
import Plaques
import Polygone
import Point
import Figure

def read(instance):

    list_files = []
    list_files.append(f"{instance}_fonderie.txt")
    list_files.append(f"{instance}_fournisseurs.txt")
    list_files.append(f"{instance}_plaques.txt")

    '''dictionnaire des données'''
    data_dict = {}

    '''dictionnaire des figures à découper'''
    dictionnaire_figures = {}
    
    print(list_files)
    for element in list_files:
        f= open(element, "r")
        with f:

            if element.find(f"{instance}_fonderie.txt") >= 0:
                r = f.readlines()
                '''on crée les alliages en stock'''
                prix_kg = r[2].strip().split()

                mv = r[3].strip().split()

                '''liste des alliages en stock'''
                liste_stock = []
                '''liste des prix'''
                liste_prix = []

                for i in range(6, len(r)):

                    pct = r[i]
                    pct.strip()
                    pct.split()
                    liste_prix.append(pct[:1])
                    pct = pct[1:]

                liste_stock.append(Alliage.Alliage(mv, prix_kg, pct))

                '''on crée la liste des toles en stock'''
                liste_tole = []
                ligne = r[0].strip().split()
                x = ligne[0]
                y = ligne[1]
                z = ligne[2]

                for alliage in liste_stock :
                    liste_tole.append(Tole.Tole(x, y, z, alliage))

                '''on crée le client'''
                pct_min = r[4].strip().split()
                pct_max = r[5].strip().split()

                client = Client.Client(pct_max, pct_min)

                cout = r[1]

                '''on crée la fonderie'''
                data_dict["fonderie"] = Fonderie.Fonderie(liste_tole, liste_stock, client, liste_prix, cout)

            elif element.find(f"{instance}_fournisseurs.txt") >= 0:
                r = f.readlines()
                '''on crée une liste de fournisseurs'''
                liste_fournisseurs : list[Fournisseur] = []
                for i in range(len(r)):
                    fournisseur = r[i].strip().split()
                    if len(fournisseur) >= 4:
                        liste_fournisseurs.append(Fournisseur.Fournisseur(fournisseur[1], fournisseur[2], fournisseur[3]))
                
                data_dict["fournisseurs"] = liste_fournisseurs

            elif element.find(f"{instance}_plaques.txt") >= 0:

                '''on crée la liste des figures à découper sur les plaques'''
                r = f.readlines()
                prix = r[0].strip().split()

                '''on crée la liste des figures à découper'''
                liste_figures : list[Figures] = []
                for i in range(1,len(r)):
                    ligne = r[i].strip().split()
                    if len(ligne) >= 2:
                        figure = ligne[0]
                        nombre = ligne[1]

                    for j in range(int(nombre)):
                        liste_figures.append(f"{figure}")

                    for k in range(int(nombre)):
                        dictionnaire_figures[f"{figure}"] = nombre

                data_dict["plaques"] = Plaques.Plaques(prix, liste_figures, 0)
                print(liste_figures)

                for figure in liste_figures:
                    l= open(f"{instance}_{figure}.txt", "r")
                    with l:
                        '''crée chacune des figures de la liste des figures'''

                        e = l.readlines()
                        dimensions = e[0].strip().split()
                        x = dimensions[0]
                        y = dimensions[1]

                        liste_polygones = []
                        for i in range(1,len(e)):
                            polygone = e[i].strip().split()
                            print(polygone)
                            liste_points : list[Point] = []
                            if len(polygone) != 0:
                                for j in range(0,len(polygone),2):
                                    if j+1 < len(polygone) :
                                        point = Point.Point(polygone[j], polygone[j+1])
                                        liste_points.append(point)
                            liste_polygones.append(liste_points)

                        nom_element = element.strip().split("_")
                        nom_element[1].split(".")

                        dictionnaire_figures[f"{nom_element[1][0]}"] = Figure.Figure(x, y, liste_polygones)
                
            else:
                continue

    return data_dict