import pygame
import time
from VieBarre import * 
from Pokemon import *
#from Dresseur import *
from Bouton import *
from JeuEtape import *
from CombatEtape import *
from CombatCurseur import *
from PokemonEnCombat import *
import Jeu

class Affichage:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Képomon")
        self.screen = pygame.display.set_mode((284*2,472*2))
        self.BLANC = (0, 0, 0)
        #background image
        self.background = pygame.image.load('assets/Gameboy.png')
        #boutons images
        self.boutonDImage = pygame.image.load('assets/boutons/boutonDroite.png')
        self.boutonGImage = pygame.image.load('assets/boutons/boutonGauche.png')
        self.boutonHImage = pygame.image.load('assets/boutons/boutonHaut.png')
        self.boutonBImage = pygame.image.load('assets/boutons/boutonBas.png')
        self.boutonRondBImage = pygame.image.load('assets/boutons/boutonRondB.png')
        self.boutonRondAImage = pygame.image.load('assets/boutons/boutonRondA.png')
        #combat images
        self.combat_truc_pour_les_personnages = pygame.image.load('assets/combat_truc_pour_les_personnages.png')
        self.combatDebutImage = pygame.image.load('assets/combatDebut.png')
        self.combat_fight = pygame.image.load('assets/combat_fight.png')
        self.combat_choosePkm = pygame.image.load('assets/combat_choosePkm.png')
        self.combat_item = pygame.image.load('assets/combat_item.png')
        self.combat_run = pygame.image.load('assets/combat_run.png')
        self.youCantRunInCombat = pygame.image.load('assets/youCantRunInCombat.png')
        self.youDontHaveAnyItems = pygame.image.load('assets/youDontHaveAnyItems.png')
        self.youExchangeYourPokemon = pygame.image.load('assets/youExchangeYourPokemon.png')

        self.chooseFirstPokemonImage = pygame.image.load('assets/chooseFirstPokemon.png')
        self.chooseSecondPokemonImage = pygame.image.load('assets/chooseSecondPokemon.png')
        self.playerAttackImage = pygame.image.load('assets/yourPokemonAttacksTheOpposingPokemon.png')
        self.botAttackImage = pygame.image.load('assets/theOpposingPokemonAttacksYourPokemon.png')
        #images personnages combat
        self.izukuCombatImageJoueur = pygame.image.load('assets/pokemonsCombat/izukuCombatJoueur.png')
        self.izukuCombatImageBot = pygame.image.load('assets/pokemonsCombat/izukuCombatBot.png')
        #index PokemonSelection
        self.pokemonSelectionPosition = 0
        #musiques/son de fond
        #clicSound = pygame.mixer.Sound('')
        self.battleMusic = pygame.mixer.music.load('assets/battleMusic.mp3')
        pygame.mixer.music.play(-1)
        #initialisation du joueur et du bot
        #create button instances
        self.boutonG = Bouton(self.screen, 103,610,self.boutonGImage,1)
        self.boutonD = Bouton(self.screen, 200,610,self.boutonDImage,1)
        self.boutonH = Bouton(self.screen, 151,559,self.boutonHImage,1)
        self.boutonB = Bouton(self.screen, 150,658,self.boutonBImage,1)
        self.boutonRondB = Bouton(self.screen, 363,637,self.boutonRondBImage,1)
        self.boutonRondA = Bouton(self.screen, 427,572,self.boutonRondAImage,1)
        #création des barres de vie
        #self.vieBarreJ = VieBarre(1,1,5,5,None)
        #self.vieBarreB = VieBarre(44,44,55,55,self.jeu.bot.getPokemons()[0])
        
        

    def flip(self):
        pygame.display.flip()


    def draw(self, jeu:Jeu):
        self.screen.blit(self.background, (0,0))

        if jeu.getJeuEtape()==JeuEtape.DEBUT:
            self.screen.blit(self.combatDebutImage,(161,168))
            if self.boutonH.draw() == True :
                pass
            if self.boutonB.draw() == True :
                pass
            if self.boutonG.draw() == True :
                pass
            if self.boutonD.draw() == True :
                pass
            if self.boutonRondB.draw() == True :
                pass
            if self.boutonRondA.draw() == True :
                jeu.setJeuEtape(JeuEtape.POKEMON_SELECTION)



        elif jeu.getJeuEtape()==JeuEtape.POKEMON_SELECTION:

            if len(jeu.p1.getPokemons()) == 0:
                self.screen.blit(self.chooseFirstPokemonImage,(161,168))
            elif len(jeu.p1.getPokemons()) == 1:
                self.screen.blit(self.chooseSecondPokemonImage,(161,168))
            

            PokemonSelectionImage = pygame.image.load(jeu.getPokemonSelectionImage(self.pokemonSelectionPosition))
            self.screen.blit(PokemonSelectionImage,(161,168))



            if self.boutonH.draw() == True :
                pass
            if self.boutonB.draw() == True :
                pass
            if self.boutonG.draw() == True :
                self.pokemonSelectionPosition=(self.pokemonSelectionPosition-1) % len(jeu.listePokemons)
                
            if self.boutonD.draw() == True :
                self.pokemonSelectionPosition=(self.pokemonSelectionPosition+1) % len(jeu.listePokemons)

            if self.boutonRondB.draw() == True :
                pass
            if self.boutonRondA.draw() == True :
                jeu.p1.setPokemon(jeu.listePokemons[self.pokemonSelectionPosition])
                jeu.listePokemons.pop(self.pokemonSelectionPosition)
                print(jeu.p1.pokemons)

                if len(jeu.p1.getPokemons())==2:
                    jeu.ajouterPokemonsBot()
                    jeu.setJeuEtape(JeuEtape.COMBAT)     



        if jeu.getJeuEtape()==JeuEtape.COMBAT:
            self.screen.blit(self.combat_truc_pour_les_personnages,(161,168))
            combatImageJoueur = pygame.image.load(jeu.p1.getPokemons()[0].getCombatImageJoueur())
            self.screen.blit(combatImageJoueur,(161,168))
            combatImageBot = pygame.image.load(jeu.bot.getPokemons()[0].getCombatImageBot())
            self.screen.blit(combatImageBot,(161,168))
        
            vieBarreJ = VieBarre(190,195,100,5,jeu.p1.getPokemons()[0].getpV(), jeu.p1.getPokemons()[0].getPvMax())
            vieBarreB = VieBarre(282,296,100,5,jeu.bot.getPokemons()[0].getpV(), jeu.bot.getPokemons()[0].getPvMax())            
            vieBarreJ.draw(self.screen)
            vieBarreB.draw(self.screen)

            pvImageJoueur = str(jeu.p1.getPokemons()[0].getpV()) + "/" + str(jeu.p1.getPokemons()[0].getPvMax())
            pvImgJoueur = pygame.font.SysFont('pokemonclassicregular', 12).render((pvImageJoueur), True, self.BLANC)
            pvImageBot = str(jeu.bot.getPokemons()[0].getpV()) + "/" + str(jeu.bot.getPokemons()[0].getPvMax())
            pvImgBot = pygame.font.SysFont('pokemonclassicregular', 12).render((pvImageBot), True, self.BLANC)
            self.screen.blit(pvImgJoueur, (290, 297)) 

            self.screen.blit(pvImgBot, (188, 197))

            nomImageJoueur = str(jeu.p1.getPokemons()[0].getNom())
            nomImgjoueur = pygame.font.SysFont('pokemonclassicregular', 12).render((nomImageJoueur), True, self.BLANC)
            nomImageBot = str(jeu.bot.getPokemons()[0].getNom())
            nomImgBot = pygame.font.SysFont('pokemonclassicregular', 12).render((nomImageBot), True, self.BLANC)
            self.screen.blit(nomImgjoueur, (273, 275))
            self.screen.blit(nomImgBot, (173, 165))

            
            
            
            if jeu.getCombatEtape() == CombatEtape.INACTIF:
            
                if jeu.getCombatCurseur() == CombatCurseur.COMBAT_RUN :
                    self.screen.blit(self.combat_run,(161,168))
                    if self.boutonH.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_PKMN)
                    if self.boutonG.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_ITEM)
                    if self.boutonRondA.draw()== True :
                        jeu.setCombatEtape(CombatEtape.IMAGE_RUN)
                    
                if jeu.getCombatCurseur() == CombatCurseur.COMBAT_ITEM :
                    self.screen.blit(self.combat_item,(161,168))
                    if self.boutonRondA.draw() == True :
                        jeu.setCombatEtape(CombatEtape.IMAGE_ITEMS)
                    if self.boutonH.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_FIGHT)
                    if self.boutonD.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_RUN)
                    

                if jeu.getCombatCurseur() == CombatCurseur.COMBAT_PKMN :
                    self.screen.blit(self.combat_choosePkm,(161,168))
                    
                    if self.boutonRondA.draw() == True :
                        jeu.setCombatEtape(CombatEtape.IMAGE_PKMNCHANGE)

                    if self.boutonG.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_FIGHT)
                    
                    if self.boutonB.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_RUN)
                    

                if jeu.getCombatCurseur() == CombatCurseur.COMBAT_FIGHT :
                    self.screen.blit(self.combat_fight,(161,168))

                    if self.boutonD.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_PKMN)
                    
                    if self.boutonB.draw() == True :
                        jeu.setCombatCurseur(CombatCurseur.COMBAT_ITEM)

                    if self.boutonRondA.draw() == True :
                        jeu.setCombatEtape(CombatEtape.JOUEUR_ATTAQUE)
            
                if self.boutonH.draw() == True :
                    pass
                if self.boutonG.draw() == True :
                        pass
                if self.boutonD.draw() == True :
                    pass
                if self.boutonRondA.draw() == True :
                    pass
                if self.boutonRondB.draw() == True :
                    pass
                if self.boutonB.draw() == True :
                    pass
            
            if jeu.getCombatEtape() == CombatEtape.IMAGE_RUN:
                self.screen.blit(self.youCantRunInCombat,(161,168))
                if self.boutonRondA.draw() == True : 
                    jeu.setCombatEtape(CombatEtape.INACTIF)
                if self.boutonRondB.draw() == True :
                    pass
                if self.boutonH.draw() == True :
                    pass
                if self.boutonG.draw() == True :
                    pass
                if self.boutonD.draw() == True :
                    pass
                if self.boutonB.draw() == True :
                    pass

            if jeu.getCombatEtape() == CombatEtape.IMAGE_ITEMS:
                self.screen.blit(self.youDontHaveAnyItems,(161,168))
                if self.boutonRondA.draw() == True : 
                    jeu.setCombatEtape(CombatEtape.INACTIF)
                if self.boutonRondB.draw() == True :
                    pass
                if self.boutonH.draw() == True :
                    pass
                if self.boutonG.draw() == True :
                    pass
                if self.boutonD.draw() == True :
                    pass
                if self.boutonB.draw() == True :
                    pass

            if jeu.getCombatEtape() == CombatEtape.IMAGE_PKMNCHANGE:
                self.screen.blit(self.youExchangeYourPokemon,(161,168))
                if self.boutonRondA.draw() == True : 
                    jeu.setCombatEtape(CombatEtape.INACTIF)
                    jeu.p1.echangerPokemons()
                if self.boutonRondB.draw() == True :
                    pass
                if self.boutonH.draw() == True :
                    pass
                if self.boutonG.draw() == True :
                    pass
                if self.boutonD.draw() == True :
                    pass
                if self.boutonB.draw() == True :
                    pass


            if jeu.getCombatEtape() == CombatEtape.JOUEUR_ATTAQUE :
                self.screen.blit(self.playerAttackImage,(161,168))
                
                if self.boutonRondA.draw() == True :   
                    jeu.p1.getPokemons()[0].attaquer(jeu.bot.getPokemons()[0])
                    if jeu.bot.getPokemons()[0].getpV() <= 0 :
                        #mettre une image "votre adversaire change de pokémon"
                        jeu.bot.echangerPokemons()
                        jeu.setCombatEtape(CombatEtape.INACTIF)
                    else :
                        jeu.setCombatEtape(CombatEtape.BOT_ATTAQUE)
            
            if jeu.getCombatEtape() == CombatEtape.BOT_ATTAQUE :
                self.screen.blit(self.botAttackImage,(161,168))
                
                if self.boutonRondA.draw() == True :

                    jeu.bot.getPokemons()[0].attaquer(jeu.p1.getPokemons()[0])
                    if jeu.p1.getPokemons()[0].getpV() <= 0 :
                        #mettre une image "vous changez de pokémon"
                        jeu.p1.echangerPokemons()
                    jeu.setCombatEtape(CombatEtape.INACTIF)

            
            if jeu.combatFin():
                #mettre une image "vous avez gagné" ou "vous avez perdu"
                
                jeu.setJeuEtape(JeuEtape.FIN_COMBAT)

        if jeu.getJeuEtape()==JeuEtape.FIN_COMBAT:
            self.screen.blit(self.combat_fight,(161,168))