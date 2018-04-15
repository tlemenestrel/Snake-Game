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

x = [0]
y = [0]
step = 10

#Création d'un grand nombre de rangs au sein de la liste pour éventuellement agrandir le corps du serpent jusqu'à 1000 sections
for i in range(0,1000):
	x.append(-100)
	y.append(-100)

#fonction définissant si il y a une collision entre les coordonnées du serpent et d'autres coordonnées
def collision(x1,y1,x2,y2, size_snake, size_fruit):
	if ((x1 + size_snake >= x2) or (x1 >= x2)) and x1 <= x2 + size_fruit:
		if ((y1 >= y2) or (y1 + size_snake >=y2)) and y1 <= y2 + size_fruit:
			return True
		return False
	
#Fonction qui affiche le score du joueur sur la page de jeu	
def disp_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, (0, 0, 0))
    fenetre.blit(text,(600,0)) 

#Initialisation de la bibliothèques Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((700, 700))
fenetre_rect = fenetre.get_rect()

#On donne un nom à la fenêtre
pygame.display.set_caption("Snake")

#On charge la musique du jeu
musique= pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play()

#On charge un fond noir avec lequel on remplit la fenêtre
couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

# On charge un personnage qu'on colle sur la fenêtre par dessus le fond noir
head = pygame.image.load("head.png").convert_alpha()
head = pygame.transform.scale(head, (35,35))
fenetre.blit(head, (0,0))

corps1 = pygame.image.load("corps.png").convert_alpha()
corps1 = pygame.transform.scale(corps1, (25,25))
fenetre.blit(corps1, (5,35))
corps2 = pygame.image.load("corps.png").convert_alpha()
corps2 = pygame.transform.scale(corps2, (25,25))
fenetre.blit(corps2, (5,60))
Personnage4 = pygame.image.load("corps.png").convert_alpha()
Personnage4 = pygame.transform.scale(Personnage4, (25,25))
fenetre.blit(Personnage4, (5,85))

fruit = pygame.image.load("square.jpg").convert()
fenetre.blit(fruit, (250,250))

# On récupère sa position
position_1 = head.get_rect()
position_fruit = fruit.get_rect()

x[0] = position_1.x
y[0] = position_1.y

score = 0
length = 3

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

    for i in range(length-1,0,-1):
        x[i] = x[i-1]
        y[i] = y[i-1]

    couverture.fill((250, 250, 250))
    for i in range(0,length):
        couverture.blit(corps1, (x[i], y[i]))
    

	# Modification de la position de la tête du serpent       
    if depUp:
        y[0] = y[0] - step
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(head, (x[0], y[0]))
        pygame.display.flip()
    if depDown:
        y[0] = y[0] + step
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(head, (x[0], y[0]))
        pygame.display.flip()
    if depRight:
        x[0] = x[0] + step
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(head, (x[0], y[0]))
        pygame.display.flip()
    if depLeft:
        x[0] = x[0] - step
        pygame.time.delay(10)
        fenetre.blit(couverture, (0,0))
        fenetre.blit(head, (x[0], y[0]))
        pygame.display.flip()

    if x[0] < fenetre_rect.left: #Ici, on vérifie si le serpent ne touche pas les bords
        continuer = False
    if x[0] > fenetre_rect.bottom:
        continuer = False
    if y[0] < fenetre_rect.top:
        continuer = False
    if y[0] > fenetre_rect.bottom:
        continuer = False

    fenetre.blit(fruit, position_fruit)
    pygame.display.flip()

    for i in range(0,length):
        if collision(position_fruit.x, position_fruit.y, x[i], y[i],35,25):
        	position_fruit.x = randint(1,670)
        	position_fruit.y = randint(1,670)
        	length = length + 1
        	score = score + 1
		
    #Vérifie si la tête du serpent ne touche pas le corps
    for i in range(2,length):
            if collision(x[0], y[0], x[i], y[i],0,0) and move_init:
                continuer = False
		
    disp_score(score)
    pygame.display.flip()

# On re-colle la fenêtre
fenetre.blit(couverture, (0,0))

pygame.display.flip()
pygame.quit()
