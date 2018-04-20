#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Snake - v0.1
# Ce script est un programme du jeu snake
# License libre CC
# Colin Laganier - Thomas Le Menestrel - 2018.03.27

#Importation des bibliothèques nécessaires
from pygame.locals import *
from random import randint
import pygame
import time

x = [0]
y = [0]
step = 23 
score = 0
highscore = 0
length = 3
etat = 1

#Création d'un grand nombre de rangs au sein de la liste pour éventuellement agrandir le corps du serpent jusqu'à 1000 sections
for i in range(0,1000):
    x.append(-100)
    y.append(-100)

#Fonction définissant si il y a une collision entre les coordonnées du serpent et d'autres coordonnées, comme celles des fruits ou des différentes parties du serpent
def collision(x1,y1,x2,y2, size_snake, size_fruit):
    if ((x1 + size_snake >= x2) or (x1 >= x2)) and x1 <= x2 + size_fruit:
        if ((y1 >= y2) or (y1 + size_snake >=y2)) and y1 <= y2 + size_fruit:
            return True
        return False

#Fonction qui affiche le score du joueur sur la page de jeu 
def disp_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, (0, 0, 0))
    fenetre.blit(text,(400,0)) 

#Fonction qui centre le texte donnée entre deux coordonnées
def disp_text(info,x,y):
    font18 = pygame.font.SysFont(None, 18)
    text = font18.render((info),True,(0,0,0))
    textX = text.get_rect().width
    textY = text.get_rect().height
    fenetre.blit(text,((x - (textX / 2)),(y - (textY / 2))))

#Initialisation de la bibliothèques Pygame
pygame.init()

#Chargement des bruitages du jeu
bruit_mouvement = pygame.mixer.Sound("move.wav")
bruit_collision = pygame.mixer.Sound("collision.wav")

#Création de la fenêtre
fenetre = pygame.display.set_mode((500, 500))
fenetre_rect = fenetre.get_rect()

#La fenêtre de jeu est nommée
pygame.display.set_caption("Snake")

#Chargement d'un fond blanc avec lequel la fenêtre est remplit
couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

#Chargement des images des différents objets du jeu
head = pygame.image.load("head.png").convert_alpha() # La tête
head = pygame.transform.scale(head, (35,35))
corps1 = pygame.image.load("corps.png").convert_alpha() #Le corps
corps1 = pygame.transform.scale(corps1, (25,25))
fruit = pygame.image.load("fruit.png").convert_alpha() #Le fruit
fruit = pygame.transform.scale(fruit, (35,35))

#Récuperation de leur position
position_1 = head.get_rect()
position_fruit = fruit.get_rect()

#Insertion des coordonnées de la tête dans leur liste respective 
x[0] = position_1.x
y[0] = position_1.y

#Position aléatoire est donnée au premier fruit, proche du joueur
position_fruit.x = randint(2,10)*step
position_fruit.y = randint(2,10)*step

#Rafraichissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle principale du jeu
continuer = True
depUp = depDown = depRight = depLeft = move_init = False

while(continuer):
    for event in pygame.event.get(): #Récupération des différents évènements du joueur
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):#Vérification de si le joueur ne quitte pas le jeu
            continuer = False
        if event.type == pygame.KEYDOWN:#Vérification de si le joueur appuye sur une des touches du clavier
        
            if event.key == pygame.K_UP:
                if etat == 2:
                    if depUp == False and move_init == True:
                        depDown = depRight = depLeft = False
                        depUp = move_init = True
                        pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_DOWN:
                if etat == 2:
                    if depDown == False:
                        depRight = depLeft = depUp = False
                        depDown = move_init = True
                        pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_RIGHT:
                if etat == 2:
                    if depRight == False:
                        depLeft = depUp = depDown = False
                        depRight = move_init = True
                        pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_LEFT:
                if etat == 2:
                    if depLeft == False:
                        depRight = depDown = depUp = False
                        depLeft = move_init = True
                        pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_RETURN:
                couverture.fill((250,250,250))
                fenetre.blit(couverture, (0,0))
                pygame.display.flip()
                
                if etat == 1:
                    etat = 2

                #Remise de tous les paramètres du jeu à ceux de départ pour la nouvelle partie
                if etat == 3:
                    depUp = depDown = depRight = depLeft = move_init = False
                    length = 3
                    for i in range (2, 1000):
                        x[i] = y[i] = -100
                    x[0] = y[0] = 0
                    x[1] = -5
                    y[1] = 5
                    position_fruit.x = randint(2,10)*step
                    position_fruit.y = randint(2,10)*step
                    score = 0
                    etat = 2

            #Définition d'une commande pour retourner au menu de depart apres avoir joué
            if event.key == pygame.K_SPACE:
                if etat == 3:
                    depUp = depDown = depRight = depLeft = move_init = False
                    length = 3
                    for i in range (2, 1000):
                        x[i] = y[i] = -100
                    x[0] = y[0] = 0
                    x[1] = -5
                    y[1] = 5
                    position_fruit.x = randint(2,10)*step
                    position_fruit.y = randint(2,10)*step
                    score = 0
                    etat = 1
                    
    #Etat du Menu principale 
    if etat == 1:

        #Chargement du fond d'écran du menu
        couverture_menu = pygame.image.load("fond2.png").convert()
        fenetre.blit(couverture_menu, (0,0))

        #Carré est déssiné pour donner les informations au joueur
        pygame.draw.rect(fenetre,(0,255,0),(290,290,200,200))
        pygame.draw.rect(fenetre,(0,200,0),(290,290,200,200),5)

        #Explication au joueur de comment entre dans le jeu 
        disp_text("Appuyez sur Entrer pour jouer",390,320)

        #Explication au joueur de quels touches utiliser pour jouer
        text = font18.render("Commandes de jeu :",True,(0,0,0))
        fenetre. blit(text, (300,360))
        controls = pygame.image.load("keypad.png").convert_alpha()
        controls = pygame.transform.scale(controls, (100,100))
        fenetre.blit(controls, (340,380))
        pygame.display.flip()                                        
    
    #Etat du jeu en cours
    if etat == 2:

        #Chargement des objets dans le jeu
        fenetre.blit(corps1, (-5,5))
        fenetre.blit(head, (0,0))
            
        #Coordonnées du morceau précédent données à chaque morceau 
        for i in range(length-1,0,-1):
            x[i] = x[i-1]
            y[i] = y[i-1]

        couverture.fill((250, 250, 250)) #Remplissage de l'écran en blanc pour effacer les parties du corps précédentes
        for i in range(0,length): #Chargement du corps du serpent
            couverture.blit(corps1, (x[i], y[i]))
        
        # Modification de la position de la tête du serpent       
        if depUp:
        
            y[0] = y[0] - step #Déplacement de la position de la tête
            fenetre.blit(couverture, (0,0)) #Chargement du fond d'écrant et de la tête
            fenetre.blit(head, (x[0], y[0]))
        
        if depDown:
        
            y[0] = y[0] + step 
            fenetre.blit(couverture, (0,0)) 
            fenetre.blit(head, (x[0], y[0]))
        
        if depRight:
        
            x[0] = x[0] + step
            fenetre.blit(couverture, (0,0)) 
            fenetre.blit(head, (x[0], y[0]))
        
        if depLeft:
        
            x[0] = x[0] - step
            fenetre.blit(couverture, (0,0)) 
            fenetre.blit(head, (x[0], y[0]))

        #Verification que le serpent ne touche pas les bords
        if x[0] < fenetre_rect.left: 
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if x[0] > fenetre_rect.bottom:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if y[0] < fenetre_rect.top:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if y[0] > fenetre_rect.bottom:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        
        #Charegement du fruit
        fenetre.blit(fruit, position_fruit)
        
        #Verification de si le serpent touche un fruit
        for i in range(0,length):
            if collision(position_fruit.x, position_fruit.y, x[i], y[i],35,25):
                position_fruit.x = randint(1,20)*step   #Nouvelles coordonnées du fruit lorsqu'il est "mangé"
                position_fruit.y = randint(1,20)*step
                length = length + 2
                score = score + 1
                    
        #Vérification de si la tête du serpent touche un morceau du corps
        for i in range(2,length):
                if collision(x[0], y[0], x[i], y[i],0,0) and move_init:
                    pygame.mixer.Sound.play(bruit_collision)
                    etat = 3
            
        #Ajout du score à l'écran
        disp_score(score)
        #Definition du meilleur score parmi les parties jouées
        if score > highscore:
            highscore = score
        
        pygame.display.flip()

        #Ajout d'un retard à la boucle pour obtenir la vitesse de déplacement voulue
        time.sleep (75.0 / 1000.0)

    if etat == 3:
        
        #Chargement d'un cadre pour donner les informations au joueur
        pygame.draw.rect(fenetre,(0,255,0),(150,150,200,200))
        pygame.draw.rect(fenetre,(0,200,0),(150,150,200,200),5)

        #Chargement du score de la partie terminé dans le cadre
        disp_text("Score: " + str(score),250,180)

        #Chargement du meilleur score parmi les parties réalisés dans le cadre
        disp_text("Meilleur score : " + str(highscore),250,230)

        #Explication au joueur pour comment rejouer 
        disp_text("Pour rejouer appuyez sur Entrer !",250, 280)

        #Explication au joueur pour comment retourner au menu
        disp_text("Pour retourner au menu appuyez", 250,305)
        disp_text("sur la barre d'espace !",250,320)

        pygame.display.flip()

#Sortie du jeu
pygame.quit()
