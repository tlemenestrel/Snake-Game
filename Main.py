#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640, 480))

Couverture = pygame.image.load("/Users/TLM/Documents/Projet ISN/fond_noir.jpg").convert()
Couverture.blit(Couverture, (0,0))

Personnage1 = pygame.image.load("/Users/TLM/Documents/Projet ISN/Toad.jpeg").convert_alpha()
#Chargement et collage du personnage
position_perso1 = Personnage1.get_rect()
Couverture.blit(Personnage1, position_perso1)

#Rafraîchissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:
                position_perso1.move(0,3)

Couverture.blit(Couverture, (0,0))	
Couverture.blit(Personnage1, position_perso1)
pygame.display.flip()
