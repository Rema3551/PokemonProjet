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
        """renvoie les pokemons du joueur
        >>> p1=Dresseur()
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> p1.getPokemons()
        []
        >>> p1.setPokemon(jessy)
        >>> p1.getPokemons()
        [JESSY]
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> p1.setPokemon(olivier)
        >>> p1.getPokemons()
        [JESSY, OLIVIER]
        """
        return self.pokemons
        
    def setPokemon(self,pokemon:Pokemon):
        """ajoute un pokemon au joueur
        >>> p1=Dresseur()
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> p1.getPokemons()
        []
        >>> p1.setPokemon(jessy)
        >>> p1.getPokemons()
        [JESSY]
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> p1.setPokemon(olivier)
        >>> p1.getPokemons()
        [JESSY, OLIVIER]
        """
        self.pokemons.append(pokemon)
    
    def echangerPokemons(self):
        """échange les pokémons du joueur
        >>> p1=Dresseur()
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> p1.getPokemons()
        []
        >>> p1.setPokemon(jessy)
        >>> p1.setPokemon(olivier)
        >>> p1.getPokemons()
        [JESSY, OLIVIER]
        >>> p1.echangerPokemons()
        >>> p1.getPokemons()
        [OLIVIER, JESSY]
        >>>
        """
        self.pokemons=[self.pokemons[1],self.pokemons[0]]
