#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Snake - v0.1
# Ce script est un programme du jeu snake
# License libre CC
# Colin Laganier - Thomas Le Menestrel - 2018.03.27

#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from random import randint

#Initialisation de la bibliothèques Pygame
pygame.init()

#CrÃ©ation de la fenÃªtre
fenetre = pygame.display.set_mode((700, 700))

#On donne un nom à la fenêtre
pygame.display.set_caption("Snake")

#On charge un fond noir avec lequel on remplit la fenêtre
couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

# On charge un personnage qu'on colle sur la fenêtre par dessus le fond noir
Personnage1 = pygame.image.load("F:\ISN\head.png").convert_alpha()
Personnage1 = pygame.transform.scale(Personnage1, (30,30))
fenetre.blit(Personnage1, (0,0))

# On récupère sa position
position_perso1 = Personnage1.get_rect()

#Rafraichissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle
continuer = True
depUp = depDown = depRight = depLeft = False

while(continuer):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                depUp = True
            if event.key == pygame.K_DOWN:
                depDown = True
            if event.key == pygame.K_RIGHT:
                depRight = True
            if event.key == pygame.K_LEFT:
                depLeft = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                depUp = False
            if event.key == pygame.K_DOWN:
                depDown = False
            if event.key == pygame.K_RIGHT:
                depRight = False
            if event.key == pygame.K_LEFT:
                depLeft = False
        if depUp:
            print("up")
        if depDown:
            print("Down")
        if depRight:
            print("right")
        if depLeft:
            print("left")

#Variable qui continue la boucle
continuer = True

# On re-colle la fenêtre
fenetre.blit(couverture, (0,0))

# On recolle le personnage à sa nouvelle position
fenetre.blit(Personnage1, position_perso1)

pygame.display.flip()
pygame.quit()
