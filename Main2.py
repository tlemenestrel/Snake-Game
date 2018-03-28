# Snake - v0.1
# Ce script est un programme du jeu snake
# License libre CC
# Colin Laganier - Thomas Le Menestrel - 2018.03.27

#Importation des bibliothèques nécessaires

import pygame
from pygame.locals import *
from random import randint
import Move
import Variables
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

Personnage1 = pygame.image.load("head.png").convert_alpha()
Personnage1 = pygame.transform.scale(Personnage1, (30,30))
fenetre.blit(Personnage1, (350,350))

# On récupère sa position pour s'en servir plus tard

position_perso1 = Personnage1.get_rect()

#Rafraîchissement de l'écran

pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0

continuer = True

#Boucle infinie

while continuer == True:

    for event in pygame.event.get():  #On parcours la liste de tous les événements reçus

        if event.type == KEYDOWN:

            if event.key == K_UP:
                runninghaut = True
                runningbas = False
                runningdroite = False
                runninggauche = False

            elif event.key == K_DOWN:
                runninghaut = False
                runningbas = True
                runningdroite = False
                runninggauche = False

            elif event.key == K_LEFT:
                runninghaut = False
                runningbas = False
                runningdroite = False
                runninggauche = True

            elif event.key == K_RIGHT:
                runninghaut = False
                runningbas = False
                runningdroite = True
                runninggauche = False


    # On re-colle la fenêtre
    while runninghaut == True:
        dephaut()
    while runningbas == True:
        depbas()
    while runninggauche == True:
        depgauche()
    while runningdroite == True:
        depdroite()
    fenetre.blit(couverture, (0,0))

    # On recolle le personnage à sa nouvelle position

    fenetre.blit(Personnage1, position_perso1)
    pygame.display.flip()
    pygame.quit()
