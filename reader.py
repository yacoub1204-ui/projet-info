import Client
import Fonderie
import Alliage
import Tole
import Fournisseur
import Plaques
import Polygone
import Point
import Figure

def read(instance, list_files):
    for element in list_files:
        f= open(element, "r")
        with f:

            '''dictionnaire des figures à découper'''
            figures = {}

            if element.find(f"{instance}_fonderie") >= 0:
                r = f.readlines()
                '''on crée les alliages en stock'''
                i_pkg = r[2]
                i_pkg.strip()
                i_pkg.split()

                i_mv = r[3]
                i_mv.strip()
                i_mv.split()

                '''liste des alliages en stock'''
                l_a_stock = []
                '''liste des prix'''
                l_prix = []

                for i in range(6, len(r)):

                    i_pct = r[i]
                    i_pct.strip()
                    i_pct.split()
                    l_prix.append = i_pct[:1]
                    i_pct = i_pct[1:]

                l_a_stock.append = Alliage.Alliage(i_mv, i_pkg, i_pct)

                '''on crée la liste des toles possibles'''
                l_tole = []
                i_tole = r[0]
                i_tole.strip()
                i_tole.split()

                for all in l_a_stock :
                    l_tole.append = Tole.Tole(i_tole[0], i_tole[1], i_tole[2], all)

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
                fonderie = Fonderie.Fonderie(l_tole, l_a_stock, client, l_prix, i_cout)

            elif element.find(f"{instance}_fournisseurs") >= 0:
                r = f.readlines()
                '''on crée un dictionnaire de fournisseurs'''
                d_fournisseurs : dict[Fournisseur] = {}
                for i in range(len(r)):
                    i_fi = r[i]
                    i_fi.strip()
                    i_fi.split()
                    d_fournisseurs[i_fi[0]] = Fournisseur.Fournisseur(i_fi[1], i_fi[2], i_fi[3])

            elif element.find(f"{instance}_") >= 0:
                r = f.readlines()

                '''on crée la figure représentée par le fichier'''

                i_dim = r[0]
                i_dim.strip()
                i_dim.split()

                list_pol : list[Polygone] = []
                for i in range(1,len(r)):
                    i_pol = r[i]
                    i_pol.strip()
                    i_pol.split("  ")
                    list_p : list[Point] = []
                    for j in range(len(i_pol)):
                        i_pol[j].split()
                        i_point = Point.Point(pol[j][0], pol[j][1])
                        list_p.append(i_point)
                    list_pol.append(list_p)

                nom_element = element
                nom_element.strip()
                nom_element.split("_")
                nom_element[1].split(".")
                figures[f"{nom_element[1][0]}"] = Figure.Figure(i_dim[0], i_dim[1], list_pol)

            elif element.find(f"{instance}_plaques") >= 0:

                '''on crée la liste des figures à découper sur les plaques'''
                r = f.readlines()
                i_prix = r[0]
                i_prix.strip()
                i_prix.split()
                '''on crée la liste des figures à découper'''
                l_fig : list[Figures] = []
                for i in range(1,len(r)):
                    i_pi = r[i]
                    i_pi.strip()
                    i_pi.split()
                    for j in range(i_pi[1]):
                        l_fig.append(f"{i_pi[0]}")

                plaques = Plaques.Plaques(i_prix[0], l_fig)
                
            else:
                raise(ValueError)