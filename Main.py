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

#Création de la fenÃªtre
fenetre = pygame.display.set_mode((700, 700))
fenetre_rect = fenetre.get_rect()

#On donne un nom à la fenêtre
pygame.display.set_caption("Snake")

#On charge un fond noir avec lequel on remplit la fenêtre
couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

# On charge un personnage qu'on colle sur la fenêtre par dessus le fond noir
Personnage1 = pygame.image.load("head.png").convert_alpha()
Personnage1 = pygame.transform.scale(Personnage1, (35,35))
fenetre.blit(Personnage1, (0,0))

corps1 = pygame.image.load("corps.png").convert_alpha()
corps1 = pygame.transform.scale(corps1, (25,25))
fenetre.blit(corps1, (5,35))
corps2 = pygame.image.load("corps.png").convert_alpha()
corps2 = pygame.transform.scale(corps2, (25,25))
fenetre.blit(corps2, (5,60))
Personnage4 = pygame.image.load("corps.png").convert_alpha()
Personnage4 = pygame.transform.scale(Personnage4, (25,25))
fenetre.blit(Personnage4, (5,85))
fruit = pygame.image.load("fruit.png").convert_alpha()
fruit = pygame.transform.scale(fruit, (25,25))
fenetre.blit(fruit, (255,0))

# On récupère sa position
position_perso1 = Personnage1.get_rect()
position_corps1 = corps1.get_rect()
position_corps2 = corps2.get_rect()
position_fruit = fruit.get_rect()

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
                depDown = depRight = depLeft = False
                depUp = True
            if event.key == pygame.K_DOWN:
            	depRight = depLeft = depUp = False
            	depDown = True
            if event.key == pygame.K_RIGHT:
            	depLeft = depUp = depDown = False
            	depRight = True
            if event.key == pygame.K_LEFT:
            	depRight = depDown = depUp = False
            	depLeft = True

    if depUp:
        position_perso1 = position_perso1.move(0,-1)
        position_corps1 = position_corps1.move(0,-1)
        position_corps2 = position_corps2.move(0,-1)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(Personnage1, position_perso1)
        fenetre.blit(corps1, position_corps1)
        fenetre.blit(corps2, position_corps2)
        pygame.display.flip()
    if depDown:
        position_perso1 = position_perso1.move(0,1)
        position_corps1 = position_corps1.move(0,1)
        position_corps2 = position_corps2.move(0,1)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(Personnage1, position_perso1)
        fenetre.blit(corps1, position_corps1)
        fenetre.blit(corps2, position_corps2)
        pygame.display.flip()
    if depRight:
        position_perso1 = position_perso1.move(1,0)
        position_corps1 = position_corps1.move(1,0)
        position_corps2 = position_corps2.move(1,0)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(Personnage1, position_perso1)
        fenetre.blit(corps1, position_corps1)
        fenetre.blit(corps2, position_corps2)
        pygame.display.flip()
    if depLeft:
        position_perso1 = position_perso1.move(-1,0)
        position_corps1 = position_corps1.move(-1,0)
        position_corps2 = position_corps2.move(-1,0)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(Personnage1, position_perso1)
        fenetre.blit(corps1, position_corps1)
        fenetre.blit(corps2, position_corps2)
        pygame.display.flip()

    if position_perso1.colliderect(position_fruit):
    	print("collision")

    if position_perso1.left < fenetre_rect.left:
        continuer = False
    if position_perso1.right > fenetre_rect.bottom:
        continuer = False
    if position_perso1.top < fenetre_rect.top:
        continuer = False
    if position_perso1.bottom > fenetre_rect.bottom:
        continuer = False

#Variable qui continue la boucle
continuer = True

# On re-colle la fenêtre
fenetre.blit(couverture, (0,0))

# On recolle le personnage à sa nouvelle position
fenetre.blit(Personnage1, position_perso1)

pygame.display.flip()
pygame.quit()
