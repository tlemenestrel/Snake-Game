#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Snake")

Couverture = pygame.image.load("/Users/TLM/Documents/Projet ISN/fond_noir.jpg").convert()
fenetre.blit(Couverture, (0,0))

Personnage1 = pygame.image.load("/Users/TLM/Documents/Projet ISN/Serpent2.png").convert_alpha()
#Chargement et collage du personnage
fenetre.blit(Personnage1, (250,250))
position_perso1 = Personnage1.get_rect()

#Rafraîchissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:                   
    for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
        if event.type == QUIT:
               continuer = 0
        if event.type == KEYUP :
            if event.key == K_ESCAPE:
                continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:
                position_perso1 = position_perso1.move(0,-10)
            if event.key == K_DOWN:
                position_perso1 = position_perso1.move(0,10)
            if event.key == K_LEFT:
                position_perso1 = position_perso1.move(-10,0)
            if event.key == K_RIGHT:
                position_perso1 = position_perso1.move(10,0)

    fenetre.blit(Couverture, (0,0))	
    fenetre.blit(Personnage1, position_perso1)
    pygame.display.flip()

pygame.quit()
