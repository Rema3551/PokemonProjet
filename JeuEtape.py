from enum import Enum

class JeuEtape(Enum):
    """
    détermine à quelle étape du jeu se trouve le programme
    """
    DEBUT = 0
    POKEMON_SELECTION = 1
    COMBAT = 2
    FIN_COMBAT = 3
    