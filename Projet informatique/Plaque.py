import polygone

class Plaque:

    def __init__(self, x : float, y : float, fig : Polygone):
        self._x = x
        self._y = y
        self._fig = fig

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_fig(self):
        return self._fig


"""
fonctoin origine plaque (coordonnees du point en bas a gauche de la plaque)

initialement:(0,0) <- en bas a gauche de la tole
ensuite l'origine devient le point le plus a gauche de la tole juste au dessus de la derniere plaque decoupee -> derniere origine + (max_y,0)
ensuite si on peut rien decouper a l'origine precedente, l'origine devient le point a droite de toutes les plaques precedemment decoupees et tout en bas -> (0,max(max_x))
ensuite on fait remonter l'origine comme au debut-> iteration donc parler eventuellement de max(max_y)) pour etre au dessus de differentes plaques
"""


def rotation(self):   
   return(Plaque(self._y,self._x,self._fig)) 
"""
    nouveau_min_x=min_x
    nouveau_max_x=nouveau_min_x + (max_y-min_y)


    nouveau_min_y=min_y
    nouveau_max_y=nouveau_min_y +(max_x-min_x)
"""
