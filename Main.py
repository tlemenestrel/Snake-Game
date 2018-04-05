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

#On démarre la musique
musique= pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play()

#Création de la fenÃªtre
fenetre = pygame.display.set_mode((700, 700))
fenetre_rect = fenetre.get_rect()

#On donne un nom à la fenêtre
pygame.display.set_caption("Snake")

#On charge un fond blanc avec lequel on remplit la fenêtre
couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

# On charge la tête du serpent
tete = pygame.image.load("head.png").convert_alpha()
tete = pygame.transform.scale(tete, (35,35))
fenetre.blit(tete, (0,0))

#On charge le corps du serpent
corps1 = pygame.image.load("corps.png").convert_alpha()
corps1 = pygame.transform.scale(corps1, (25,25))
fenetre.blit(corps1, (5,35))

#On charge un fruit
fruit = pygame.image.load("fruit.png").convert_alpha()
fruit = pygame.transform.scale(fruit, (25,25))
fenetre.blit(fruit, (255,0))

# On récupère sa position
position_1 = tete.get_rect()
position_2 = corps1.get_rect()
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
            if event.key == pygame.K_UP: #On vérifie si le joueur appuye sur une des flèches
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
    #Ici, on effectue le déplacement du serpent 
    if depUp:
        
        position_1 = position_1.move(0,-1)
        position_2 = position_2.move(0,-1)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(tete, position_1)
        fenetre.blit(corps1, position_2)
        pygame.display.flip()
        
    if depDown:
        
        position_1 = position_1.move(0,1)
        position_2 = position_2.move(0,1)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(tete, position_1)
        fenetre.blit(corps1, position_2)
        pygame.display.flip()
        
    if depRight:
        position_1 = position_1.move(1,0)
        position_2 = position_2.move(1,0)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(tete, position_1)
        fenetre.blit(corps1, position_2)
        pygame.display.flip()
        
    if depLeft:
        position_1 = position_1.move(-1,0)
        position_2 = position_2.move(-1,0)
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(tete, position_1)
        fenetre.blit(corps1, position_2)
        pygame.display.flip()

    if position_1.colliderect(position_fruit):
    	print("collision")

    if position_1.left < fenetre_rect.left: #Ici, on vérifie si le serpent ne touche pas les bords
        continuer = False
    if position_1.right > fenetre_rect.bottom:
        continuer = False
    if position_1.top < fenetre_rect.top:
        continuer = False
    if position_1.bottom > fenetre_rect.bottom:
        continuer = False

#Variable qui continue la boucle
continuer = True

# On re-colle la fenêtre
fenetre.blit(couverture, (0,0))

# On recolle le personnage à sa nouvelle position
fenetre.blit(tete, position_1)

pygame.display.flip()
pygame.quit()
