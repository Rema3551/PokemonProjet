#https://online.visual-paradigm.com/w/hbwsawpb/diagrams/#diagram:workspace=hbwsawpb&proj=0&id=1&type=ClassDiagram
"""
from Pokemon import *
from Dresseur import *
from JeuEtape import *
from PokemonEnCombat import *
"""
from Jeu import *



jeu = Jeu()



running = True

while running:

    jeu.print()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")