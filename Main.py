
#Importation des bibliothèques nécessaires

import pygame
from pygame.locals import *
from random import randint



#Initialisation de la bibliothèque Pygame

pygame.init()



#Création de la fenêtre

fenetre = pygame.display.set_mode((700, 700))



#On donne un nom à la fenêtre

pygame.display.set_caption("Snake")



#On charge un fond noir avec lequel on remplit la fenêtre

Couverture = pygame.image.load("/Users/TLM/Documents/ProjetISN/fond_noir.jpg").convert()

fenetre.blit(Couverture, (0,0))



# On charge un personnage qu'on colle sur la fenêtre par dessus le fond noir

Personnage1 = pygame.image.load("/Users/TLM/Documents/ProjetISN/Serpent2.png").convert_alpha()

fenetre.blit(Personnage1, (250,250))



# On récupère sa position pour s'en servir plus tard

position_perso1 = Personnage1.get_rect()



#Rafraîchissement de l'écran

pygame.display.flip()

pygame.time.set_timer(USEREVENT+1, 100)

#Variable qui continue la boucle si = 1, stoppe si = 0

continuer = 1



#Boucle infinie

while continuer:

    for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
        if event.type == USEREVENT+1
        
            Bananne = pygame.image.load ("/Users/TLM/Documents/ProjetISN/Banane.png").convert_alpha
            fenetre.blit(Banane, (randomint(0,700),randomint(0, 700)))                 
        if event.type == QUIT:

               continuer = 0

        if event.type == KEYUP :

            if event.key == K_ESCAPE:

                continuer = 0

        # Ensemble des touches qui permettent de déplacer le personnage

        if event.type == KEYDOWN:

            if event.key == K_UP:
                for i in range (1,300):
                    position_perso1 = position_perso1.move(0,-1)
                    fenetre.blit(Personnage1, position_perso1)
                    pygame.time.delay(10)
                    pygame.display.flip()

            if event.key == K_DOWN:
              for i in range (1,300):
                    position_perso1 = position_perso1.move(0,1)
                    fenetre.blit(Personnage1, position_perso1)
                    pygame.time.delay(10)
                    pygame.display.flip()

            if event.key == K_LEFT:
                for i in range (1,300):
                    position_perso1 = position_perso1.move(-1,0)
                    fenetre.blit(Personnage1, position_perso1)
                    pygame.time.delay(10)
                    pygame.display.flip()

            if event.key == K_RIGHT:
                for i in range (1,300):
                    position_perso1 = position_perso1.move(1,0)
                    fenetre.blit(Personnage1, position_perso1)
                    pygame.time.delay(10)
                    pygame.display.flip()



    # On re-colle la fenêtre

    fenetre.blit(Couverture, (0,0))



    # On recolle le personnage à sa nouvelle position

    fenetre.blit(Personnage1, position_perso1)

    pygame.display.flip()



pygame.quit()
