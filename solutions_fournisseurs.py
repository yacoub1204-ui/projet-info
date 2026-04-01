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
            if epsilon1 > 0 and epsilon2 < 0
                liste_achat1.append(0)
            elif epsilon1 > 0:
                liste_achat1.append(alliage.get_list_prix[i] * epsilon1)
            elif epsilon2 < 0:
                liste_achat1.append(alliage.get_list_prix[i] * epsilon2)
            count = 0
            for _ in liste_achat1 :
                count +=1
            liste_prix_achats.append(count)