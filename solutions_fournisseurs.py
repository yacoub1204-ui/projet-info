import Fonderie
import Plaques
import pulp

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
            if epsilon1 > 0 and epsilon2 < 0 :
                liste_achat1.append(0)
            elif epsilon1 > 0:
                liste_achat1.append(alliage.get_list_prix[i] * epsilon1)
            elif epsilon2 < 0:
                liste_achat1.append(alliage.get_list_prix[i] * epsilon2)
            count = 0
            for _ in liste_achat1 :
                count +=1
            liste_prix_achats.append(count)

def triviale3(fonderie : Fonderie, plaques : Plaques):
    nombre_plaques = len(plaques.get_liste_f())
    volume_plaque = fonderie.get_list_tole()[0].get_x() * fonderie.get_list_tole()[0].get_y() * fonderie.get_list_tole()[0].get_z()
    liste_prix = []
    liste_solution = []
    for j in range(len(fonderie.get_list_all())):
        '''on boucle sur le nombre d'alliages'''
        prix_achat = 0
        liste_achats = []

        for i in range(len(fonderie.get_liste_all()[j].get_liste_pct())):
            '''on récupère le prix d'achat de chaque métal en choisissant l'alliage j'''
            pct_moyen = (fonderie.get_client().get_pct_max()[i] + fonderie.get_client().get_pct_min()[i]) / 2
            masse_requise = nombre_plaques * fonderie.get_liste_all()[i].get_liste_mv()[i] * pct_moyen * volume_plaque
            masse_possedee = fonderie.get_list_kg()[j] * fonderie.get_list_all()[j].get_list_pct()[i]
            masse_achat = masse_requise - masse_possedee
            if masse_achat <=0:
                masse_achat = 0
                          
            liste_achats.append(masse_achat)
            prix_achat += masse_achat * fonderie.get_list_prix()[i]
        
        liste_prix.append(prix_achat)

def fonderie_pl(fonderie):
    """
    Résolution du problème d'optimisation de la fonderie.
    :param fonderie: objet Fonderie contenant toutes les donnees
    :param nb_toles: nombre de toles a produire
    :return: cout optimal, masses de metaux achetes, masses d'alliages utilises
    """

    # Donnees de base
    nb_toles = 30
    volume_tole = fonderie.get_tole().get_x() * fonderie.get_tole().get_y() * fonderie.get_tole().get_z()
    volume_total = nb_toles * volume_tole  # volume total de metal a fondre (cm3)

    metaux = range(len(fonderie.get_list_mat()))
    alliages = range(len(fonderie.get_list_all()))

    prix_kg = [fonderie.get_list_mat()[i].get_prix_kg() for i in metaux]
    mv_metal = [fonderie.get_list_mat()[i].get_mv() for i in metaux]
    pct_min = [fonderie.get_client().get_list_min()[i] for i in metaux]
    pct_max = [fonderie.get_client().get_list_max()[i] for i in metaux]

    # pct_all[j][i] = proportion du metal i dans l'alliage j
    pct_all = [fonderie.get_list_all()[j].get_list_pct() for j in alliages]
    # mv_all[j] = masse volumique de l'alliage j (g/cm3)
    mv_all = [fonderie.mv_alliage(j) for j in alliages]
    # stock_kg[j] = masse disponible de l'alliage j (kg)
    stock_kg = [fonderie.get_list_all()[j].get_kg() for j in alliages]

    # Modele
    modele = pulp.LpProblem("Fonderie", pulp.LpMinimize)

    # Variables de decision
    # masse_achetee[i] : kg du metal pur i achete sur le marche
    masse_achetee = [
        pulp.LpVariable(f"achat_metal_{i}", lowBound=0, cat="Continuous")
        for i in metaux
    ]
    # masse_alliage[j] : kg de l'alliage en stock j utilise
    masse_alliage = [
        pulp.LpVariable(f"alliage_{j}", lowBound=0, cat="Continuous")
        for j in alliages
    ]

    # Fonction objectif : minimiser le cout d'achat des metaux purs
    modele += pulp.lpSum(prix_kg[i] * masse_achetee[i] for i in metaux)

    # Contrainte 1 : volume total de metal suffisant pour produire les toles
    # La masse totale / masse volumique moyenne doit etre >= volume_total
    # On exprime en cm3 : sum(masse_achetee[i]*1000/mv_metal[i]) + sum(masse_alliage[j]*1000/mv_all[j]) >= volume_total
    modele += (
        pulp.lpSum(masse_achetee[i] * 1000 / mv_metal[i] for i in metaux)
        + pulp.lpSum(masse_alliage[j] * 1000 / mv_all[j] for j in alliages)
        >= volume_total
    ), "volume_suffisant"

    # masse totale en kg de metal dans la cuve
    masse_totale = (
        pulp.lpSum(masse_achetee[i] for i in metaux)
        + pulp.lpSum(masse_alliage[j] for j in alliages)
    )

    # Contrainte 2a : proportion minimale de chaque metal dans l'alliage final
    # (masse du metal i dans la cuve) >= pct_min[i] * masse_totale
    # masse du metal i = masse_achetee[i] + sum_j(pct_all[j][i] * masse_alliage[j])
    for i in metaux:
        masse_metal_i = (
            masse_achetee[i]
            + pulp.lpSum(pct_all[j][i] * masse_alliage[j] for j in alliages)
        )
        modele += masse_metal_i >= pct_min[i] * masse_totale, f"pct_min_{i}"
        modele += masse_metal_i <= pct_max[i] * masse_totale, f"pct_max_{i}"

    # Contrainte 3 : ne pas depasser le stock disponible de chaque alliage
    for j in alliages:
        modele += masse_alliage[j] <= stock_kg[j], f"stock_alliage_{j}"

    # Resolution
    modele.solve(pulp.PULP_CBC_CMD(msg=False))

    print("Resolution:", pulp.LpStatus[modele.status])
    if modele.status == pulp.constants.LpSolutionOptimal:
        cout_achat = pulp.value(modele.objective)
        cout_fonte = volume_total * fonderie.get_cout()
        cout_total = cout_achat + cout_fonte
        return [
            cout_total,
            0,
            nb_toles,
            [masse_achetee[i].varValue for i in metaux],
            [masse_alliage[j].varValue for j in alliages]
        ]
    else:
        return float('-inf'), [], []
