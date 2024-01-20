from enum import Enum

class CombatCurseur(Enum):
    """
    détermine à quelle étape du curseur se trouve le programme
    """
    COMBAT_FIGHT = 0
    COMBAT_ITEM = 1
    COMBAT_PKMN = 2
    COMBAT_RUN = 3