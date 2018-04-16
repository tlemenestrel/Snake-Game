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
step = 8
score = 0
length = 3

#Création d'un grand nombre de rangs au sein de la liste pour éventuellement agrandir le corps du serpent jusqu'à 1000 sections
for i in range(0,1000):
	x.append(-100)
	y.append(-100)

#fonction définissant si il y a une collision entre les coordonnées du serpent et d'autres coordonnées, comme celles des fruits ou des différentes parties du serpent
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

#On charge un fond noir avec lequel on remplit la fenêtre
couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

#On charge les images des différents objets du jeu
head = pygame.image.load("head.png").convert_alpha()
head = pygame.transform.scale(head, (35,35))
corps1 = pygame.image.load("corps.png").convert_alpha()
corps1 = pygame.transform.scale(corps1, (25,25))
fruit = pygame.image.load("fruit.png").convert_alpha()
fruit = pygame.transform.scale(fruit, (35,35))

#On charge les objets dans le jeu
fenetre.blit(head, (0,0))
fenetre.blit(corps1, (-5,5))

#On récupère leur position
position_1 = head.get_rect()
position_fruit = fruit.get_rect()

x[0] = position_1.x
y[0] = position_1.y
position_fruit.x = randint(1,300)
position_fruit.y = randint(1,300)

#Rafraichissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle
continuer = True
depUp = depDown = depRight = depLeft = move_init = False

while(continuer):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                depDown = depRight = depLeft = False
                depUp = move_init = True
            if event.key == pygame.K_DOWN:
            	depRight = depLeft = depUp = False
            	depDown = move_init = True
            if event.key == pygame.K_RIGHT:
            	depLeft = depUp = depDown = False
            	depRight = move_init = True
            if event.key == pygame.K_LEFT:
            	depRight = depDown = depUp = False
            	depLeft = move_init = True

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
        	length = length + 2
        	step = step + 0.5
        	score = score + 1

    # Vérifie si la tête du serpent ne touche pas le corps
    for i in range(2,length):
            if collision(x[0], y[0], x[i], y[i],0,0) and move_init:
                continuer = False
		
    disp_score(score)
    pygame.display.flip()

pygame.quit()
