import Fonderie
import Plaques

class Printer:

    def __init__(self, fonderie : Fonderie, plaques : Plaques):
        self._fonderie = fonderie
        self._plaques = plaques

    def print_fournisseurs(self, fonction):
        solution = fonction(self._fonderie, self._plaques)
        afficher = f"{solution[0]}  {solution[1]}  {solution[2]}\n"
        for i in range(3, len(solution)):
            afficher += f"{solution[i]}  "
        afficher += "\n"

        return afficher
    
    def print_plaques(self, fonction):
        solution = None
        afficher = None

    def print_figures(self, fonction):
        solution = None
        afficher = None
        for figure in self.plaques.get_list_f():
            solution = fonction(figure).copy()
            afficher = f"{figure}  "
            for i in range(len(solution)):
                afficher += f"{solution[i]}  "
            afficher += "\n"
        
        return afficher

