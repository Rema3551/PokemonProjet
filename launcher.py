from Jeu import *

jeu = Jeu()



running = True

while running:

    jeu.print()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")