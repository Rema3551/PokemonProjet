import pygame
from VieBarre import * 
from Bouton import *
from JeuEtape import *
from CombatEtape import *
from CombatCurseur import *
import Jeu

class Affichage:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Képomon") #nom du jeu
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
        #instances des boutons
        self.boutonG = Bouton(self.screen, 103,613,self.boutonGImage,1)
        self.boutonD = Bouton(self.screen, 199,613,self.boutonDImage,1)
        self.boutonH = Bouton(self.screen, 151,559,self.boutonHImage,1)
        self.boutonB = Bouton(self.screen, 151,658,self.boutonBImage,1)
        self.boutonRondB = Bouton(self.screen, 363,637,self.boutonRondBImage,1)
        self.boutonRondA = Bouton(self.screen, 427,572,self.boutonRondAImage,1)
        #index PokemonSelection
        self.pokemonSelectionPosition = 0 #pour la sélection du pokémon, j'ai utilisé un index pour savoir quel pokémon mettre dans la liste des pokemons du dresseur
        #choose pokemon image
        self.chooseFirstPokemonImage = pygame.image.load('assets/chooseFirstPokemon.png')
        self.chooseSecondPokemonImage = pygame.image.load('assets/chooseSecondPokemon.png')
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
        self.youCantExchangeYourPokemon = pygame.image.load('assets/youCantExchangeYourPokemon.png')

        self.playerAttackImage = pygame.image.load('assets/yourPokemonAttacksTheOpposingPokemon.png')
        self.botAttackImage = pygame.image.load('assets/theOpposingPokemonAttacksYourPokemon.png')
        #musiques/son de fond
        self.battleMusic = pygame.mixer.music.load('assets/battleMusic.mp3')
        pygame.mixer.music.play(-1)
        #images de fin
        self.gagneImage = pygame.image.load('assets/gagneImage.png')
        self.perduImage = pygame.image.load('assets/perduImage.png')



    def flip(self):
        pygame.display.flip()



    def draw(self, jeu:Jeu):
        """
        affichage du jeu
        """
        self.screen.blit(self.background, (0,0))

        if jeu.getJeuEtape()==JeuEtape.DEBUT:
            """
            1ere etape du jeu : l'écran de départ,
            Le joueur doit appuyer sur le bouton A pour pouvoir changer d'étape
            """
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
            """
            2eme etape du jeu : l'écran de sélection
            Le joueur peut appuyer sur les flèches directionnels pour choisir ses pokemons
            Le joueur doit appuyer sur le bouton A pour pouvoir choisir ses pokemons
            """
            #on regarde combien de pokémon possède le joueur, pour pouvoir mettre la bonne image
            if len(jeu.p1.getPokemons()) == 0: 
                self.screen.blit(self.chooseFirstPokemonImage,(161,168))
            elif len(jeu.p1.getPokemons()) == 1:
                self.screen.blit(self.chooseSecondPokemonImage,(161,168))
            
            #initialise l'image de selection du pokemon qui correspond au nombre de self.pokemonSelectionPosition. Cette image changera à chaque fois que self.pokemonSelectionPosition changera
            PokemonSelectionImage = pygame.image.load(jeu.getPokemonSelectionImage(self.pokemonSelectionPosition))
            self.screen.blit(PokemonSelectionImage,(161,168))



            if self.boutonH.draw() == True :
                pass
            if self.boutonB.draw() == True :
                pass
            if self.boutonG.draw() == True :
                #si le joueur appuie sur le bouton de gauche, self.pokemonSelectionPosition changera, donc l'image de selection changera
                self.pokemonSelectionPosition=(self.pokemonSelectionPosition-1) % len(jeu.listePokemons)
                
            if self.boutonD.draw() == True :
                #si le joueur appuie sur le bouton de droite, self.pokemonSelectionPosition changera, donc l'image de selection changera
                self.pokemonSelectionPosition=(self.pokemonSelectionPosition+1) % len(jeu.listePokemons)

            if self.boutonRondB.draw() == True :
                pass
            if self.boutonRondA.draw() == True :
                #si le joueur appuie sur le bouton A, on ajoute le pokemon correspondant à l'index self.pokemonSelectionPosition dans la liste de pokemons du dresseur
                jeu.p1.setPokemon(jeu.listePokemons[self.pokemonSelectionPosition])
                #on enlève ensuite le pokemon correspondant dans la liste de pokemon du jeu (=Pokedex)
                jeu.listePokemons.pop(self.pokemonSelectionPosition)
                self.pokemonSelectionPosition=0

                if len(jeu.p1.getPokemons())==2:
                    #si le joueur possède 2 pokemons (le nombre requis), on donne des pokemons aléatoire au bot et on change l'étape du jeu
                    jeu.ajouterPokemonsBot()
                    jeu.setJeuEtape(JeuEtape.COMBAT)     



        if jeu.getJeuEtape()==JeuEtape.COMBAT:
            """
            3eme etape du jeu : l'écran de combat
            Le joueur peut appuyer sur les flèches directionnels pour pouvoir déplacer le curseur
            Le joueur doit appuyer sur le bouton A pour soit attaquer, changer de pokemon, essayer de s'échapper et essayer d'utiliser un item
            """






















            
            self.screen.blit(self.combat_truc_pour_les_personnages,(161,168))
            combatImageJoueur = pygame.image.load(jeu.p1.getPokemons()[0].getCombatImageJoueur())
            self.screen.blit(combatImageJoueur,(161,168))
            combatImageBot = pygame.image.load(jeu.bot.getPokemons()[0].getCombatImageBot())
            self.screen.blit(combatImageBot,(161,168))
        
            vieBarreJ = VieBarre(282,296,100,5,jeu.p1.getPokemons()[0].getpV(), jeu.p1.getPokemons()[0].getPvMax())
            vieBarreB = VieBarre(190,195,100,5,jeu.bot.getPokemons()[0].getpV(), jeu.bot.getPokemons()[0].getPvMax())            
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
                        if jeu.p1.getPokemons()[0].getVitesse() > jeu.bot.getPokemons()[0].getVitesse():
                            jeu.setCombatEtape(CombatEtape.JOUEUR_ATTAQUE)
                        else :
                            jeu.setCombatEtape(CombatEtape.BOT_ATTAQUE)
            
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
                if jeu.p1.getPokemons()[0].getpV() > 0 and jeu.p1.getPokemons()[1].getpV() > 0:
                    self.screen.blit(self.youExchangeYourPokemon,(161,168))
                else:
                    self.screen.blit(self.youCantExchangeYourPokemon,(161,168))
                if self.boutonRondA.draw() == True : 
                    jeu.setCombatEtape(CombatEtape.BOT_ATTAQUE)
                    if jeu.p1.getPokemons()[0].getpV() > 0 and jeu.p1.getPokemons()[1].getpV() > 0:
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
                        if jeu.p1.getPokemons()[0].getVitesse() > jeu.bot.getPokemons()[0].getVitesse():
                            jeu.setCombatEtape(CombatEtape.BOT_ATTAQUE)
                        else :
                            jeu.setCombatEtape(CombatEtape.INACTIF)
                if self.boutonH.draw() == True :
                    pass
                if self.boutonG.draw() == True :
                    pass
                if self.boutonD.draw() == True :
                    pass
                if self.boutonB.draw() == True :
                    pass
                if self.boutonRondB.draw() == True :
                    pass
                
            
            if jeu.getCombatEtape() == CombatEtape.BOT_ATTAQUE :
                self.screen.blit(self.botAttackImage,(161,168))
                
                if self.boutonRondA.draw() == True :

                    jeu.bot.getPokemons()[0].attaquer(jeu.p1.getPokemons()[0])
                    if jeu.p1.getPokemons()[0].getpV() <= 0 :
                        #mettre une image "vous changez de pokémon"
                        jeu.p1.echangerPokemons()
                    if jeu.p1.getPokemons()[0].getVitesse() > jeu.bot.getPokemons()[0].getVitesse():
                            jeu.setCombatEtape(CombatEtape.INACTIF)
                    else :
                            jeu.setCombatEtape(CombatEtape.JOUEUR_ATTAQUE)

                if self.boutonH.draw() == True :
                    pass
                if self.boutonG.draw() == True :
                    pass
                if self.boutonD.draw() == True :
                    pass
                if self.boutonB.draw() == True :
                    pass
                if self.boutonRondB.draw() == True :
                    pass
                
            
            if jeu.combatFin():
                #mettre une image "vous avez gagné" ou "vous avez perdu"
                
                jeu.setJeuEtape(JeuEtape.FIN_COMBAT)

        if jeu.getJeuEtape()==JeuEtape.FIN_COMBAT:
            if jeu.p1.getPokemons()[0].getpV() > 0 or jeu.p1.getPokemons()[1].getpV() > 0 :
                self.screen.blit(self.gagneImage,(161,168))
            else:
                self.screen.blit(self.perduImage,(161,168))
            if self.boutonRondA.draw() == True : 
                exit()
            if self.boutonRondB.draw() == True :
                exit()
            if self.boutonH.draw() == True :
                pass
            if self.boutonG.draw() == True :
                pass
            if self.boutonD.draw() == True :
                pass
            if self.boutonB.draw() == True :
                pass