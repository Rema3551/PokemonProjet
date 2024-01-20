from enum import Enum

class CombatEtape(Enum):
    """
    détermine à quelle étape du combat se trouve le programme
    """
    INACTIF = 0
    JOUEUR_ATTAQUE = 1
    BOT_ATTAQUE = 2
    IMAGE_RUN = 3
    IMAGE_ITEMS = 4
    IMAGE_PKMNCHANGE = 5