import Fonderie
import Plaques

def triviale(fonderie : Fonderie, plaques : Plaques):

    nb_plaques = 0
    for _ in plaques:
        nb_plaques += 1
    
    tole = fonderie.get_tole()[0]
    volume_tole = tole.get_x() * tole.get_y() * fonderie.get_z()
    volume_total = nb_plaques * volume_tole
    
    cout_fonte = volume_total * fonderie.get_cout()

    cout_metaux = 0
  
    cout_total = cout_metaux + cout_fonte
    
    return nb_plaques, cout_total