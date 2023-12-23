import random
from Affichage import *
from JeuEtape import *
from CombatEtape import *
from Dresseur import *

class Jeu:

    def __init__(self):
        charmander = Pokemon("CHARMANDER", 44, 10, 50, "eau", "plante", "feu", 'assets/choisirCharmander.png', 'assets\pokemonsCombat/charmanderCombatJoueur.png','assets\pokemonsCombat/charmanderCombatBot.png')
        gon = Pokemon("GON", 44, 10, 50, "eau", "plante", "feu", 'assets/choisirGon.png', 'assets\pokemonsCombat/gonCombatJoueur.png', 'assets\pokemonsCombat/gonCombatBot.png')
        izuku = Pokemon("IZUKU", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirIzuku.png', 'assets\pokemonsCombat/izukuCombatJoueur.png', 'assets\pokemonsCombat/izukuCombatBot.png')
        soldier = Pokemon("SOLDIER", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirSoldier.png', 'assets\pokemonsCombat/soldierCombatJoueur.png', 'assets\pokemonsCombat/soldierCombatBot.png')
        jessy = Pokemon("JESSY", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        olivier = Pokemon("OLIVIER", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        raoul = Pokemon("RAOUL", 100, 5, 50, "eau", "plante", "feu", 'assets/choisirRaoul.png', 'assets\pokemonsCombat/raoulCombatJoueur.png', 'assets\pokemonsCombat/raoulCombatBot.png')
        kilyan = Pokemon("KILYAN", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirKilyan.png', 'assets\pokemonsCombat/kilyanCombatJoueur.png', 'assets\pokemonsCombat/kilyanCombatBot.png')
        titouan = Pokemon("TITOUAN", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirTitouan.png', 'assets\pokemonsCombat/titouanCombatJoueur.png', 'assets\pokemonsCombat/titouanCombatBot.png')
        professeur = Pokemon("PROFESSEUR", 200, 5, 50, "eau", "plante", "feu", 'assets/choisirProfesseur.png', 'assets\pokemonsCombat/professeurCombatJoueur.png', 'assets\pokemonsCombat/professeurCombatBot.png')

        self.listePokemons=[charmander, gon, izuku, soldier, jessy, olivier, raoul, kilyan, titouan, professeur]

        self.affichage=Affichage()
        self.jeuEtape = JeuEtape.DEBUT
        self.combatEtape = CombatEtape.COMBAT
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

        self.joueurEnTrainAttaquer = False
        self.botEnTrainAttaquer = False


    
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

    def getCombatEtape(self):
        return self.combatEtape
    
    def setCombatEtape(self, combatEtape):
        self.combatEtape=combatEtape
        
    def getPokemonSelectionImage(self, position):
        pokemon = self.listePokemons[position]
        return pokemon.selectionImage
    

    def getJoueurEnTrainAttaquer(self) -> bool:
        return self.joueurEnTrainAttaquer
    
    def setJoueurEnTrainAttaquer(self):
        if self.joueurEnTrainAttaquer == True :
            self.joueurEnTrainAttaquer = False
        else :
            self.joueurEnTrainAttaquer = True

    def getBotEnTrainAttaquer(self):
        return self.botEnTrainAttaquer

    def setBotEnTrainAttaquer(self):
        if self.botEnTrainAttaquer == True:
            self.botEnTrainAttaquer = False
        else :
            self.botEnTrainAttaquer = True

    def combatFin(self):
        if self.p1.getPokemons()[0].getpV() <= 0 and self.p1.getPokemons()[1].getpV() <= 0:
            return True
        elif self.bot.getPokemons()[0].getpV() <= 0 and self.bot.getPokemons()[1].getpV() <= 0:
            return True
        else:
            return False



    def print(self):
        self.affichage.draw(self)
        self.affichage.flip()