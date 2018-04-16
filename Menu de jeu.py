# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from Projet import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Accueil")


#BOUCLE PRINCIPALE
continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load("accueil.png").convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
	    for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                            continuer_accueil = 0
                            continuer_jeu = 0
                            continuer = 0
				
				
                    elif event.type == KEYDOWN:
                            if event.key == K_F1:
                                    continuer_accueil = 0
                                    Projet = open("Projet.py","b")
                                    Projet.read()
