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
        
        

    def getPvMax(self):
        """
        retourne le nombre de pvMax du pokémon
        """
        return self.pvMax
    
    def getpV(self):
        """
        retourne le nombre de pv du pokémon
        """
        return self.pv
    
    def getNom(self):
        """
        retourne le nom du pokémon
        """
        return self.nom

    def getVitesse(self):
        """
        retourne la vitesse du pokémon
        """
        return self.vitesse

    
    def attaquer(self,pokemon2):
        """
        attaque le pokémon adverse, donc lui enlève des pv
        """
        if self.type == pokemon2.faiblesse:
            pokemon2.pv=pokemon2.pv-(self.pA*2)
        elif self.type == pokemon2.avantage:
            pokemon2.pv=pokemon2.pv-(self.pA*2)
        else:
            pokemon2.pv=pokemon2.pv-self.pA

    def getCombatImageJoueur(self):
        """
        retourne l'image de combat du pokémon lorsque le joueur le possède
        """
        return self.combatImageJoueur
    
    def getCombatImageBot(self):
        """
        retourne l'image de combat du pokémon lorsque le bot le possède
        """
        return self.combatImageBot