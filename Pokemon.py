class Pokemon:
    """
    attributs :
        -nom
        -point de vie
        -points d'attaque (attaque de base)
        -(attaque speciale)
        -faiblesse
        -avantage
        -type
    
    methodes :
        -get...()
        -attaquer(pokemon2)

    """

    def __init__(self, nom:str, pvMax:int, pA:int, attaqSpeciale:int, type:str, avantage:str, faiblesse:str, selectionImage:str, combatImageJoueur:str, combatImageBot:str):
        self.nom=nom
        self.pvMax=pvMax
        self.pv=pvMax
        self.pA=pA
        self.attaqSpeciale=attaqSpeciale
        self.faiblesse=faiblesse 
        self.avantage=avantage
        self.type=type
        self.selectionImage=selectionImage
        self.combatImageJoueur=combatImageJoueur
        self.combatImageBot=combatImageBot
        
        

    def getPvMax(self):
        return self.pvMax
    
    def getpV(self):
        return self.pv
    
    def getNom(self):
        return self.nom
    
    def attaquer(self,pokemon2):
        if self.type == pokemon2.faiblesse:
            pokemon2.pv=pokemon2.pv-(self.pA*2)
        elif self.type == pokemon2.avantage:
            pokemon2.pv=pokemon2.pv-(self.pA*2)
        else:
            pokemon2.pv=pokemon2.pv-self.pA

    def getCombatImageJoueur(self):
        return self.combatImageJoueur
    
    def getCombatImageBot(self):
        return self.combatImageBot