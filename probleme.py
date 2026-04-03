import Printer
import reader2
import solutions_figures
import solutions_fournisseurs

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

    # CORRECTION BUG 1, 2, 3 : Generation complete du fichier solution avec le bon format
    from solution_decoupe_2 import decouper
    import math
    
    data = reader2.read(inst)
    fonderie = data["fonderie"]
    plaques  = data["plaques"]
    tole = fonderie.get_tole()[0]
    
    # ETAPE 1 : Calculer le plan de decoupe
    solution_decoupe = decouper(tole, plaques)
    nb_toles = len(solution_decoupe.get_plans())
    
    # ETAPE 2 : Calculer l'approvisionnement (fonderie)
    volume_tole = tole.get_x() * tole.get_y() * tole.get_z()
    volume_total = nb_toles * volume_tole
    
    # Choix alliage moyen selon cahier des charges client
    pct_min = fonderie.get_client().get_pct_min()
    pct_max = fonderie.get_client().get_pct_max()
    pct_moyen = [(pct_min[i] + pct_max[i]) / 2 for i in range(len(pct_min))]
    
    # Masse volumique moyenne de l'alliage (g/cm3)
    liste_materiaux = fonderie.get_liste_mat()
    masse_volumique_alliage = sum(pct_moyen[i] * liste_materiaux[i].get_mv() for i in range(len(pct_moyen)))
    masse_totale = volume_total * masse_volumique_alliage / 1000  # kg (conversion g -> kg)
    
    # Utiliser les alliages en stock puis completer avec metaux purs
    kg_metaux = [0.0] * len(liste_materiaux)
    kg_alliages = [0.0] * len(fonderie.get_list_all())
    
    masse_restante = masse_totale
    for i, alliage in enumerate(fonderie.get_list_all()):
        kg_utilisable = min(alliage.get_kg(), masse_restante)
        kg_alliages[i] = kg_utilisable
        masse_restante -= kg_utilisable
    
    # Completer avec metaux purs
    if masse_restante > 0:
        for i in range(len(pct_moyen)):
            kg_metaux[i] = masse_restante * pct_moyen[i]
    
    # ETAPE 3 : Calculer les couts
    cout_metaux = sum(kg_metaux[i] * liste_materiaux[i].get_prix_kg() for i in range(len(kg_metaux)))
    cout_fonte = volume_total * fonderie.get_cout()
    
    # ETAPE 4 : Calculer le cout laser (trajet trivial)
    cout_laser_unitaire = plaques.get_prix_d()
    cout_laser_total = 0.0
    
    # Pour chaque modele de plaque (pas chaque exemplaire)
    modeles_vus = set()
    for figure in plaques.get_list_f():
        nom = figure.get_nom()
        if nom in modeles_vus:
            continue
        modeles_vus.add(nom)
        
        # Trajet trivial : (0,0) -> premier point de chaque polygone dans l'ordre -> (0,0)
        distance = 0.0
        position_actuelle = (0.0, 0.0)
        
        for polygone in figure.get_list_poly():
            if len(polygone.get_list_points()) > 0:
                premier_point = polygone.get_list_points()[0]
                x_point = premier_point.get_x()
                y_point = premier_point.get_y()
                distance += math.sqrt((x_point - position_actuelle[0])**2 + (y_point - position_actuelle[1])**2)
                position_actuelle = (x_point, y_point)
        
        # Retour a l'origine
        distance += math.sqrt(position_actuelle[0]**2 + position_actuelle[1]**2)
        
        # Multiplier par le nombre d'exemplaires de ce modele
        nb_exemplaires = sum(1 for f in plaques.get_list_f() if f.get_nom() == nom)
        cout_laser_total += distance * cout_laser_unitaire * nb_exemplaires
    
    cout_total = cout_metaux + cout_fonte + cout_laser_total
    
    # ETAPE 5 : Ecrire le fichier solution avec le BON format
    with open(f"{inst}_sol.txt", "w") as file:
        # Ligne 1 : cout fournisseur nb_toles
        file.write(f"{cout_total:.2f} 0 {nb_toles}\n")
        
        # Ligne 2 : kg_metaux kg_alliages (seulement si fonderie)
        file.write(" ".join(f"{kg:.3f}" for kg in kg_metaux))
        file.write(" ")
        file.write(" ".join(f"{kg:.3f}" for kg in kg_alliages))
        file.write("\n")
        
        # Lignes de placement : tole_num nom x y rotation
        for tole_idx, plan in enumerate(solution_decoupe.get_plans()):
            for placement in plan.get_placements():
                figure = placement.get_figure()
                x = placement.get_x()
                y = placement.get_y()
                rotation = 1 if placement.get_tournee() else 0
                file.write(f"{tole_idx} {figure.get_nom()} {x:.2f} {y:.2f} {rotation}\n")
        
        # Lignes laser : nom poly_idx pt_idx poly_idx pt_idx ...
        modeles_vus = set()
        for figure in plaques.get_list_f():
            nom = figure.get_nom()
            if nom in modeles_vus:
                continue
            modeles_vus.add(nom)
            
            file.write(nom)
            for poly_idx, polygone in enumerate(figure.get_list_poly()):
                if len(polygone.get_list_points()) > 0:
                    file.write(f" {poly_idx} 0")  # Point d'attaque = premier point (indice 0)
            file.write("\n")
    
    duree: float = time.time() - debut
    print(f"Duree d'execution : {round(100 * duree) / 100} secondes")


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
