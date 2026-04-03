import Fonderie2
import Plaques

class Printer:

    def __init__(self, fonderie : Fonderie2, plaques : Plaques):
        self._fonderie = fonderie
        self._plaques = plaques

    def print_fournisseurs(self, fonction):
        solution = fonction(self._fonderie)
        afficher = f"{solution[0]}  {solution[1]}  {solution[2]}\n"
        # solution[3] = liste des metaux achetes, solution[4] = liste des alliages utilises
        for valeur in solution[3]:
            afficher += f"{round(valeur, 3)}  "
        for valeur in solution[4]:
            afficher += f"{round(valeur, 3)}  "
        afficher += "\n"
        return afficher
    def print_plaques(self, tole_plans):
        afficher = ""
    
        for i, plan in enumerate(tole_plans):
            for placement in plan.get_placements():
                figure = placement.get_figure()
    
                afficher += f"{i}  "
                afficher += f"{figure.get_nom()}  "
                afficher += f"{placement.get_x()}  "
                afficher += f"{placement.get_y()}  "
                afficher += f"{placement.get_tournee()}  "
                afficher += "\n"
    
        return afficher

 

    def print_figures(self, fonction):
        solution = None
        afficher = None
        for figure in self._plaques.get_list_f():
            solution = fonction(figure).copy()
            afficher = f"{figure}  "
        afficher = ""
        list_db = []
        for figure in self._plaques.get_list_f():
            if figure in list_db:
                continue
            else:
                solution = fonction(figure)
                afficher += f"{figure}  "
                for i in range(len(solution)):
                    afficher += f"{solution[i]}   "
                afficher += "\n"
                list_db.append(figure)

        return afficher
