from Pokemon import *

class Dresseur:
    """
    attributs :
        -pokemons (liste qui contient les pokémons du dresseur)
    
    methodes :
        -getPokemons(self)
        -setPokemon(self,pokemon:Pokemon)
        -echangerPokemons(self)
    """


    def __init__(self):
        self.pokemons=[]

    def getPokemons(self):
        return self.pokemons
        
    def setPokemon(self,pokemon:Pokemon):
        self.pokemons.append(pokemon)
    
    def echangerPokemons(self):
        self.pokemons=[self.pokemons[1],self.pokemons[0]]
