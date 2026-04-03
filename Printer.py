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
        """
        Genere le format de sortie pour la solution de decoupe.
        Appelle la fonction de decoupe et formate les resultats.
 
        Args:
            fonction: Fonction decouper(tole, plaques) retournant la solution
 
        Returns:
            Chaine de caracteres contenant la solution formatee :
            - Une ligne par plaque placee
            - Format : {numero_tole} {nom_plaque} {x:.3f} {y:.3f} {tournee}
            - Chaque ligne se termine par un newline
            - Vide si la solution est vide
        """
        tole = self._fonderie.get_tole()
        solution = fonction(tole, self._plaques)
 
        afficher = ""
 
        # Traiter chaque tole et ses placements
        if solution:
            for i, placements in enumerate(solution):
                # Ajouter chaque placement dans cette tole
                for p in placements:
                    # Format: num_tole nom x y tournee
                    # Les coordonnees sont affichees avec 3 decimales
                    afficher += f"{i} {p.get_figure().get_nom()} {p.get_x_origine():.3f} {p.get_y_origine():.3f} {p.get_tournee()}\n"
 
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
