class Pokemon:
    """
    attributs :
        -nom:str (nom du pokemon)
        -pvMax:int (pv maximum du pokemon)
        -pA:int (point d'attaque du pokemon)
        -attaqSpeciale:int (point d'attque de l'attaque spéciale du pokemon)
        -type:str (type du pokemon)
        -avantage:str (avantage par rapport au type du pokemon)
        -faiblesse:str (faiblesse par rapport au type du pokemon)
        -selectionImage:str (image de selection du pokemon)
        -combatImageJoueur:str (image de combat du pokemon quand le joueur le possède)
        -combatImageBot:str (image de combat du pokémon quand le bot le possède)
    
    methodes :
        -getPvMax(self)
        -getpV(self)
        -getNom(self)
        -attaquer(self,pokemon2)
        -getCombatImageJoueur(self)
        -getCombatImageBot(self)
    """

    def __init__(self, nom:str, pvMax:int, pA:int, attaqSpeciale:int, vitesse:int, type:str, avantage:str, faiblesse:str, selectionImage:str, combatImageJoueur:str, combatImageBot:str):
        self.nom=nom
        self.pvMax=pvMax
        self.pv=pvMax
        self.pA=pA
        self.vitesse=vitesse
        self.attaqSpeciale=attaqSpeciale
        self.faiblesse=faiblesse 
        self.avantage=avantage
        self.type=type
        self.selectionImage=selectionImage
        self.combatImageJoueur=combatImageJoueur
        self.combatImageBot=combatImageBot
        
    def __str__(self):
        """le str renvoie seulement le nom"""
        return self.nom

    def getPvMax(self):
        """
        retourne le nombre de pvMax du pokémon
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> raoul = Pokemon("RAOUL", 50, 15, 50, 3,"plante", "feu", "eau", 'assets/choisirRaoul.png', 'assets\pokemonsCombat/raoulCombatJoueur.png', 'assets\pokemonsCombat/raoulCombatBot.png')
        >>> kilyan = Pokemon("KILYAN", 50, 15, 50, 4, "eau", "plante", "feu", 'assets/choisirKilyan.png', 'assets\pokemonsCombat/kilyanCombatJoueur.png', 'assets\pokemonsCombat/kilyanCombatBot.png')
        >>> titouan = Pokemon("TITOUAN", 50, 15, 50, 5, "feu", "eau", "plante", 'assets/choisirTitouan.png', 'assets\pokemonsCombat/titouanCombatJoueur.png', 'assets\pokemonsCombat/titouanCombatBot.png')
        >>> professeur = Pokemon("PROFESSEUR", 50, 15, 50, 6, "plante", "feu", "eau", 'assets/choisirProfesseur.png', 'assets\pokemonsCombat/professeurCombatJoueur.png', 'assets\pokemonsCombat/professeurCombatBot.png')
        >>> jessy.getPvMax()
        50
        >>> olivier.getPvMax()
        50
        >>> raoul.getPvMax()
        50
        >>> kilyan.getPvMax()
        50
        >>> titouan.getPvMax()
        50
        >>> professeur.getPvMax()
        50
        """
        return self.pvMax
    
    def getpV(self):
        """
        retourne le nombre de pv du pokémon
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> jessy.getpV()
        50
        >>> olivier.attaquer(jessy)
        >>> jessy.getpV()
        20
        """
        return self.pv
    
    def getNom(self):
        """
        retourne le nom du pokémon
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> jessy.getNom()
        'JESSY'
        >>> olivier.getNom()
        'OLIVIER'
        """
        return self.nom

    def getVitesse(self):
        """
        retourne la vitesse du pokémon
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> jessy.getVitesse()
        1
        >>> olivier.getVitesse()
        2
        
        """
        return self.vitesse

    
    def attaquer(self,pokemon2):
        """
        attaque le pokémon adverse, donc lui enlève des pv
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> jessy.getpV()
        50
        >>> olivier.getpV()
        50
        >>> olivier.attaquer(jessy)
        >>> jessy.getpV()
        20
        >>> jessy.attaquer(olivier)
        >>> olivier.getpV()
        43
        """
        if self.type == pokemon2.faiblesse:
            pokemon2.pv=pokemon2.pv-(self.pA*2)
        elif self.type == pokemon2.avantage:
            pokemon2.pv=pokemon2.pv-(self.pA//2)
        else:
            pokemon2.pv=pokemon2.pv-self.pA

    def getCombatImageJoueur(self):
        """
        retourne l'image de combat du pokémon lorsque le joueur le possède
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> jessy.getCombatImageJoueur()
        'assets\\pokemonsCombat/jessyCombatJoueur.png'
        >>> olivier.getCombatImageJoueur()
        'assets\\pokemonsCombat/olivierCombatJoueur.png'
        """
        return self.combatImageJoueur
    
    def getCombatImageBot(self):
        """
        retourne l'image de combat du pokémon lorsque le bot le possède
        >>> jessy = Pokemon("JESSY", 50, 15, 50, 1, "eau", "plante", "feu", 'assets/choisirJessy.png', 'assets\pokemonsCombat/jessyCombatJoueur.png', 'assets\pokemonsCombat/jessyCombatBot.png')
        >>> olivier = Pokemon("OLIVIER", 50, 15, 50, 2, "feu", "eau", "plante", 'assets/choisirOlivier.png', 'assets\pokemonsCombat/olivierCombatJoueur.png', 'assets\pokemonsCombat/olivierCombatBot.png')
        >>> jessy.getCombatImageBot()
        'assets\\pokemonsCombat/jessyCombatBot.png'
        >>> olivier.getCombatImageBot()
        'assets\\pokemonsCombat/olivierCombatBot.png'
        """
        return self.combatImageBot