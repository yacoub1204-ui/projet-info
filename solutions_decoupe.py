import Plaques

def solutiondecoupedecoupetr(tole : Tole, plaques : Plaques):
    tole_x = tole.get_x()
    tole_y = tole.get_y()

    list_f = plaques.get_list_f()
    
    placement = []
    n_tole = 0
    
    for nom, dim_x, dim_y, n in list_f:
        for _ in range(n):
           
            if dim_x < dim_y:
                tourne = 1
            else:
                tourne = 0
            
            placement.append([n_tole, nom, 0.0, 0.0, tourne])
            n_tole += 1
    
    return placement, n_tole