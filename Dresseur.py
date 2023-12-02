from Pokemon import *

class Dresseur:
    """
    attributs :
        -pokemons
    
    methodes :
        -changerPokemon()
        -choisirPokemon()
        -botPokemon()
    """


    def __init__(self):
        self.pokemons=[]
        self.pokemonsEnCombat=None

    def getPokemons(self):
        return self.pokemons
        
    def setPokemon(self,pokemon:Pokemon):
        self.pokemons.append(pokemon)

    def getPokemonsEnCombat(self):
        return self.pokemonsEnCombat

    def setPokemonEnCombat(self, pokemonEnCombat):
        self.pokemonsEnCombat = pokemonEnCombat