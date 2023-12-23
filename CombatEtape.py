from enum import Enum

class CombatEtape(Enum):
    COMBAT_FIGHT = 0
    COMBAT_ITEM = 1
    COMBAT_PKMN = 2
    COMBAT_RUN = 3
    JOUEUR_ATTAQUE = 4
    BOT_ATTAQUE = 5