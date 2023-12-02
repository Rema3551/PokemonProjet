import random
from Affichage import *
from JeuEtape import *
from Dresseur import *

class Jeu:

    def __init__(self):
        charmander = Pokemon("CHARMANDER", 44, 10, 50, "eau", "plante", "feu", 'assets/choisirCharmander.png', None, None)
        gon = Pokemon("GON", 44, 10, 50, "eau", "plante", "feu", 'assets/choisirGon.png', None, None)
        izuku = Pokemon("IZUKU", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirIzuku.png', 'assets\pokemonsCombat/izukuCombatJoueur.png', 'assets\pokemonsCombat/izukuCombatBot.png' )
        soldier = Pokemon("SOLDIER", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirSoldier.png', 'assets\pokemonsCombat/soldierCombatJoueur.png', None)
        jessy = Pokemon("JESSY", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirJessy.png', None, None)
        olivier = Pokemon("OLIVIER", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirOlivier.png', None, None)

        self.listePokemons=[charmander, gon, izuku, soldier, jessy, olivier]

        self.affichage=Affichage()
        self.jeuEtape = JeuEtape.DEBUT

        self.p1=Dresseur()
        self.bot=Dresseur()
        
        self.pj1=""
        self.pj2=""
        self.pokemonEnCombatJ = PokemonEnCombat.PJC1

        self.pokemonsBot=random.shuffle(self.listePokemons)
        self.bot.setPokemon(self.listePokemons[0])
        self.bot.setPokemon(self.listePokemons[1])
        print(self.bot.getPokemons()[0].nom)
        print(self.bot.getPokemons()[1].nom)

        self.pokemonEnCombatB = PokemonEnCombat.PBC1

    
    def getPj1(self):
        return self.pj1
    
    def setPj1(self,pj1):
        self.pj1=pj1

    def getPj2(self):
        return self.pj2
    
    def setPj2(self,pj2):
        self.pj2=pj2

    def getPj1pvMax(self):
        return

    def setJeuEtape(self,jeuEtape):
        self.jeuEtape=jeuEtape

    def getJeuEtape(self):
        return self.jeuEtape
    
    def getPokemonSelectionImage(self, position):
        pokemon = self.listePokemons[position]
        return pokemon.selectionImage
        #if getPokemonSelection() == nombres de pokemon présent dans la liste:
        #setPokemonSelection(0)
        #modulo
        #setPokemonSelection(getPokemonSelection()-1)
    
    




    def print(self):
        self.affichage.draw(self)
        self.affichage.flip()        