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
        
    def print_plaques(self, solution):

        output = []
        
        # Parcours chaque tôle
        for tole_idx, plan in enumerate(solution.get_plans()):
            # Parcours chaque figure placée dans cette tôle
            for placement in plan.get_placements():
                figure = placement.get_figure()
                nom = figure.get_nom()
                x = placement.get_x()
                y = placement.get_y()
                tournee = 1 if placement.get_tournee() else 0
                
                # Format: numéro_tole nom_figure x y tournee
                output.append(f"{tole_idx} {nom} {x:.2f} {y:.2f} {tournee}")
        
        return "\n".join(output)
    
   

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
