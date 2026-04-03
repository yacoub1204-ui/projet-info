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
        solution_decoupe = fonction(self._fonderie, self._plaques)

        tole = self._fonderie.get_tole()
        solution = fonction(tole, self._plaques)
    
        afficher = ""
        for numero_tole, plan in enumerate(solution.get_plans()):
            for p in plan.get_placements():
                nom = p.get_figure().get_nom()
                x = p.get_x()
                y = p.get_y()
                if p.get_tournee()==1:
                    tourne=1
                else:
                    tourne= 0
                afficher += f"{numero_tole}  {nom}  {x}  {y}  {tourne}\n"
        return afficher
    
   

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
