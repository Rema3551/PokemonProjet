from enum import Enum

class CombatEtape(Enum):
    INACTIF = 0
    JOUEUR_ATTAQUE = 1
    BOT_ATTAQUE = 2