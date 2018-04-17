# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *

pygame.init()


#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Accueil")


#BOUCLE PRINCIPALE
continuer_accueil = 1
while continuer_accueil:
    accueil = pygame.image.load("accueil.png").convert()
    fenetre.blit(accueil, (0,0))

	#Rafraichissement
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer_accueil = 0
				
				
        elif event.type == KEYDOWN:
            if event.key == K_a:
                from Projet import*
                
                
pygame.quit()

