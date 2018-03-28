# Snake - v0.1
# Ce script est un programme du jeu snake
# License libre CC
# Colin Laganier - Thomas Le Menestrel - 2018.03.27

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

#On charge un fond noir avec lequel on remplit la fenetre

couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

# On charge un personnage qu'on colle sur la fenetre par dessus le fond noir

Personnage1 = pygame.image.load("/Users/colinlaganier/Desktop/head.png").convert_alpha()
Personnage1 = pygame.transform.scale(Personnage1, (30,30))
fenetre.blit(Personnage1, (350,350))

# On récupère sa position pour s'en servir plus tard

position_perso1 = Personnage1.get_rect()

#Rafraîchissement de l'écran

pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0

continuer = True

runningdroit = False
runningauche = False
runningbas = False
runninghaut = False 

#Boucle infinie

while continuer:

    for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
                             
        if event.type == QUIT:

               continuer = False

        if event.type == KEYUP :

            if event.key == K_ESCAPE:

                continuer = False

        # Ensemble des touches qui permettent de déplacer le personnage
        
        runningdroit = False
        runningauche = False
        runningbas = False
        runninghaut = False
        
        if event.type == KEYDOWN:
    
            if event.key == K_UP:
                runninghaut = True
                runningbas = False
                runningdroite = False
                runninggauche = False

            if event.key == K_DOWN:
                runninghaut = False
                runningbas = True
                runningdroite = False
                runninggauche = False

            if event.key == K_LEFT:
                runninghaut = False
                runningbas = False
                runningdroite = False
                runninggauche = True

            if event.key == K_RIGHT:
                runninghaut = False
                runningbas = False
                runningdroite = True
                runninggauche = False
                
            while runninghaut == True:
                    for i in range (1,300):
                        position_perso1 = position_perso1.move(0,-1)
                        fenetre.blit(Personnage1, position_perso1)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    if runninghaut == False:
                        break
                    
            while runningbas == True:
                    for i in range (1,300):
                         position_perso1 = position_perso1.move(0,1)
                         fenetre.blit(Personnage1, position_perso1)
                         pygame.time.delay(10)
                         pygame.display.flip()
                    if runningbas == False:
                        break
                    
            while runninggauche == True:
                    for i in range (1,300):
                        position_perso1 = position_perso1.move(-1,0)
                        fenetre.blit(Personnage1, position_perso1)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    if runninggauche == False:
                        break
                        
            while runningdroit == True:
                    for i in range (1,300):
                        position_perso1 = position_perso1.move(1,0)
                        fenetre.blit(Personnage1, position_perso1)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    if runningdroit == False:
                        break
    # On re-colle la fenêtre

    fenetre.blit(Couverture, (0,0))

    # On recolle le personnage à sa nouvelle position

    fenetre.blit(Personnage1, position_perso1)
    pygame.display.flip()
    pygame.quit()
