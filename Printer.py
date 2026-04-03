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
    
    def print_plaques(self, fonction):
        solution = None
        afficher = None

   # Dans Printer.py
    def print_figures(self, fonction):
        afficher = ""
        for figure in self._plaques.get_list_f():
            solutions = fonction(figure)  # Doit retourner une liste de solutions
            
            for solution in solutions:
                afficher += f"{figure}  "
                for valeur in solution:
                    afficher += f"{valeur}   "
                afficher += "\n"
        return afficher
