import Plaques

class Solution :

    def __init__(self, fonderie, tole, plaque):
        self._fonderie = fonderie
        self._tole = tole
        self._plaque = plaque

    def solution_tr(self):
        list_tole = self._fonderie.sol_tr()
        list_plaque = self._tole.sol_tr()
        decoupe = self._figure.decoupe_tr()