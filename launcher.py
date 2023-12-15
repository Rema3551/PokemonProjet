#https://online.visual-paradigm.com/w/hbwsawpb/diagrams/#diagram:workspace=hbwsawpb&proj=0&id=1&type=ClassDiagram

from Pokemon import *
from Dresseur import *
from JeuEtape import *
from Jeu import *
from PokemonEnCombat import *


jeu = Jeu()

"""
p1=Dresseur()
bot=Dresseur()
bot.hasard()
print(bot.getPokemonsDresseur())
pb1=Pokemon(bot.getPokemonsDresseur()[0])
#pb1=Pokemon(bot.getPokemonsDresseur()[0])
pb2=Pokemon(bot.getPokemonsDresseur()[1])
print(pb1.getNom())
print(pb2.getNom())
"""



running = True

while running:

    jeu.print()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")