import random
from Affichage import *
from JeuEtape import *
from CombatEtape import *
from CombatCurseur import *
from Dresseur import *
from Pokemon import *
class Jeu:

    def __init__(self):
        """
        charmander = Pokemon("CHARMANDER", 44, 10, 50, "eau", "plante", "feu", 'assets/choisirCharmander.png', 'assets\pokemonsCombat/charmanderCombatJoueur.png','assets\pokemonsCombat/charmanderCombatBot.png')
        gon = Pokemon("GON", 44, 10, 50, "eau", "plante", "feu", 'assets/choisirGon.png', 'assets\pokemonsCombat/gonCombatJoueur.png', 'assets\pokemonsCombat/gonCombatBot.png')
        izuku = Pokemon("IZUKU", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirIzuku.png', 'assets\pokemonsCombat/izukuCombatJoueur.png', 'assets\pokemonsCombat/izukuCombatBot.png')
        soldier = Pokemon("SOLDIER", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirSoldier.png', 'assets\pokemonsCombat/soldierCombatJoueur.png', 'assets\pokemonsCombat/soldierCombatBot.png')
        """
        jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        raoul = Pokemon("RAOUL", 50, 15, 50, 3,"plante", "feu", "eau", 'assets/choisirRaoul.png', 'assets\pokemonsCombat/raoulCombatJoueur.png', 'assets\pokemonsCombat/raoulCombatBot.png')
        kilyan = Pokemon("KILYAN", 50, 15, 50, 4, "eau", "plante", "feu", 'assets/choisirKilyan.png', 'assets\pokemonsCombat/kilyanCombatJoueur.png', 'assets\pokemonsCombat/kilyanCombatBot.png')
        titouan = Pokemon("TITOUAN", 50, 15, 50, 5, "feu", "eau", "plante", 'assets/choisirTitouan.png', 'assets\pokemonsCombat/titouanCombatJoueur.png', 'assets\pokemonsCombat/titouanCombatBot.png')
        professeur = Pokemon("PROFESSEUR", 50, 15, 50, 6, "plante", "feu", "eau", 'assets/choisirProfesseur.png', 'assets\pokemonsCombat/professeurCombatJoueur.png', 'assets\pokemonsCombat/professeurCombatBot.png')

        self.listePokemons=[jessy, olivier, raoul, kilyan, titouan, professeur] # ajouter charmander, gon, izuku, soldier, pour les avoir

        self.affichage=Affichage()
        self.jeuEtape = JeuEtape.DEBUT
        self.combatEtape = CombatEtape.INACTIF
        self.combatCurseur = CombatCurseur.COMBAT_FIGHT
        self.p1=Dresseur()
        self.bot=Dresseur()

    def setJeuEtape(self,jeuEtape):
        """change l'étape du jeu
        >>> jeu = Jeu()
        >>> jeu.getJeuEtape()
        <JeuEtape.DEBUT: 0>
        >>> jeu.setJeuEtape(JeuEtape.COMBAT)
        >>> jeu.getJeuEtape()
        <JeuEtape.COMBAT: 2>
        """
        self.jeuEtape=jeuEtape

    def getJeuEtape(self):
        """retourne l'étape du jeu
        >>> jeu = Jeu()
        >>> jeu.getJeuEtape()
        <JeuEtape.DEBUT: 0>
        >>> jeu.setJeuEtape(JeuEtape.COMBAT)
        >>> jeu.getJeuEtape()
        <JeuEtape.COMBAT: 2>
        """
        return self.jeuEtape

    def getCombatEtape(self):
        """retourne l'étape du combat
        >>> jeu = Jeu()
        >>> jeu.getCombatEtape()
        <CombatEtape.INACTIF: 0>
        >>> jeu.setCombatEtape(CombatEtape.JOUEUR_ATTAQUE)
        >>> jeu.getCombatEtape()
        <CombatEtape.JOUEUR_ATTAQUE: 1>
        """
        return self.combatEtape
    
    def setCombatEtape(self, combatEtape):
        """change l'étape du combat
        >>> jeu = Jeu()
        >>> jeu.getCombatEtape()
        <CombatEtape.INACTIF: 0>
        >>> jeu.setCombatEtape(CombatEtape.JOUEUR_ATTAQUE)
        >>> jeu.getCombatEtape()
        <CombatEtape.JOUEUR_ATTAQUE: 1>
        """
        self.combatEtape=combatEtape

    def getCombatCurseur(self):
        """renvoie "l'étape" du curseur
        >>> jeu = Jeu()
        >>> jeu.getCombatCurseur()
        <CombatCurseur.COMBAT_FIGHT: 0>
        >>> jeu.setCombatCurseur(CombatCurseur.COMBAT_ITEM)
        >>> jeu.getCombatCurseur()
        <CombatCurseur.COMBAT_ITEM: 1>
        """
        return self.combatCurseur

    def setCombatCurseur(self, combatCurseur):
        """change "l'étape" du curseur
        >>> jeu = Jeu()
        >>> jeu.getCombatCurseur()
        <CombatCurseur.COMBAT_FIGHT: 0>
        >>> jeu.setCombatCurseur(CombatCurseur.COMBAT_ITEM)
        >>> jeu.getCombatCurseur()
        <CombatCurseur.COMBAT_ITEM: 1>
        """
        self.combatCurseur=combatCurseur

    def getPokemonSelectionImage(self, position):
        """index
        >>> jeu = Jeu()
        >>> jeu.getPokemonSelectionImage(0)
        'assets/choisirJessy.png'
        >>> jeu.getPokemonSelectionImage(3)
        'assets/choisirKilyan.png'
        >>> jeu.getPokemonSelectionImage(4)
        'assets/choisirTitouan.png'
        >>> jeu.getPokemonSelectionImage(5)
        'assets/choisirProfesseur.png'
        >>> jeu.getPokemonSelectionImage(1)
        'assets/choisirOlivier.png'
        """
        pokemon = self.listePokemons[position]
        return pokemon.selectionImage
    

    def combatFin(self)->bool:
        """renvoie si c'est la fin du combat ou non"""
        if self.p1.getPokemons()[0].getpV() <= 0 and self.p1.getPokemons()[1].getpV() <= 0:
            return True
        elif self.bot.getPokemons()[0].getpV() <= 0 and self.bot.getPokemons()[1].getpV() <= 0:
            return True
        else:
            return False


    def ajouterPokemonsBot(self):
        """ajoute des pokemons aléatoires au bot
        >>> jeu=Jeu()
        >>> jeu.ajouterPokemonsBot()
        >>> jeu.bot.getPokemons()[0].getNom()
        'TITOUAN'
        >>> jeu.bot.getPokemons()[1].getNom()
        'JESSY'
        """
        self.pokemonsBot=random.shuffle(self.listePokemons)
        self.bot.setPokemon(self.listePokemons[0])
        self.bot.setPokemon(self.listePokemons[1])
        self.listePokemons.pop(1)
        self.listePokemons.pop(0)

    def print(self):
        self.affichage.draw(self)
        self.affichage.flip()