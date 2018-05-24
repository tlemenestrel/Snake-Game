#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Snake - v2.1
# Ce script est un programme du jeu snake
# License libre CC BY 4.0
# Colin Laganier - Thomas Le Menestrel - 2018.05.13

#Importation des bibliothèques nécessaires
from pygame.locals import *
from random import randint
import pygame
import time

#Définition des variables intervenant dans le jeu
x = [0]
y = [0]
step = 23
score = 0
highscore = 0
length = 3
etat = 1
menu = 1
size_barre = 70
vitesse = 75.0

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

#Chargement d'un fond blanc avec lequel la fenêtre est remplie
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
#Changement de la variable de déplacement
while(continuer):
    for event in pygame.event.get(): #Récupération des différents évènements du joueur
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):#Vérification de si le joueur ne quitte pas le jeu
            continuer = False
        if event.type == pygame.KEYDOWN:#Vérification de si le joueur appuye sur une des touches du clavier

            if event.key == pygame.K_UP:
                if etat == 2: #Vérification de si le programme est à l'état de jeu
                    if depUp == False and move_init == True:#Vérification que la direction soit différente et annonce que les déplacement on débutés
                        if depDown == True:# Empêchement d'aller dans la direction opposée
                            depUp == False
                        else:
                            depDown = depRight = depLeft = False #Changement de la variable de déplacement
                            depUp = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_DOWN:
                if etat == 2:
                    if depDown == False:# Empêchement d'aller dans la direction opposée
                        if depUp == True:
                            depDown == False
                        else:
                            depRight = depLeft = depUp = False #Changement de la variable de déplacement
                            depDown = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_RIGHT:
                if etat == 1 and menu == 3:
                    if size_barre >=0 and size_barre <=130:
                        size_barre = size_barre + 10
                        vitesse = vitesse - 7.5
                if etat == 2:
                    if depRight == False: # Empêchement d'aller dans la direction opposée
                        if depLeft == True:
                            depRight == False
                        else:
                            depLeft = depUp = depDown = False #Changement de la variable de déplacement
                            depRight = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_LEFT:
                if etat == 1 and menu == 3:
                    if size_barre >=10 and size_barre <=140:
                        size_barre = size_barre - 10
                        vitesse = vitesse + 7.5
                if etat == 2:
                    if depLeft == False:
                        if depRight == True:# Empêchement d'aller dans la direction opposée
                            depLeft == False
                        else:
                            depRight = depDown = depUp = False #Changement de la variable de déplacement
                            depLeft = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_RETURN:
                #Remplissage de l'écran en blanc pour effacer les parties du corps précédentes
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
                if etat == 1:
                    if menu == 2 or menu == 3 or menu == 4:
                        menu = 1
                if etat == 3: #Si le joueur perd
                    depUp = depDown = depRight = depLeft = move_init = False #Les variables de déplacement deviennent fausses
                    length = 3 #Remise de tous les paramètres du jeu à ceux de départ pour la nouvelle partie
                    for i in range (2, 1000):
                        x[i] = y[i] = -100
                    x[0] = y[0] = 0
                    x[1] = -5
                    y[1] = 5
                    position_fruit.x = randint(2,10)*step
                    position_fruit.y = randint(2,10)*step
                    score = 0
                    etat = menu = 1

            if event.key == pygame.K_c: #Accès à la page des contrôles
                if etat == 1 and menu == 1:
                    menu = 2

            if event.key == pygame.K_p:#Accès à la page des paramètres
                if etat == 1 and menu == 1:
                    menu = 3

            if event.key == pygame.K_r:#Possibilité de remettre la vitesse à sa valeur initiale
                if etat == 1 and menu == 3:
                    size_barre = 70
                    vitesse = 75.0
            if event.key == pygame.K_w:#Accès à la page des crédits
                if etat == 1 and menu == 1:
                    menu = 4

    #Etat du Menu principale
    if etat == 1:

        #Chargement du fond d'écran du menu
        couverture_menu = pygame.image.load("fond2.png").convert()
        fenetre.blit(couverture_menu, (0,0))

        if menu == 1:
            #Carré est déssiné pour donner les informations au joueur
            pygame.draw.rect(fenetre,(0,255,0),(290,290,200,200))
            pygame.draw.rect(fenetre,(0,200,0),(290,290,200,200),5)

            #Explication au joueur de comment entre dans le jeu
            disp_text("Appuyez sur Entrer pour jouer",390,320)

            #Explication au joueur de quels touches utiliser pour jouer
            disp_text("Appuyez sur C pour voir les",390,360)
            disp_text("commandes",390,380)
            disp_text("Appuyez sur P pour les",390,420)
            disp_text("paramètres",390,440)
            font14 = pygame.font.SysFont(None, 14)
            text = font14.render("Appuyez sur W pour les crédits",True,(0,0,0))
            fenetre. blit(text, (320,470))
            pygame.display.flip()

        if menu == 2:
            #Carré est déssiné pour donner les informations au joueur
            pygame.draw.rect(fenetre,(0,255,0),(290,290,200,200))
            pygame.draw.rect(fenetre,(0,200,0),(290,290,200,200),5)

            #Explication au joueur comment jouer
            disp_text("Commandes de jeu :",390,310)
            font18 = pygame.font.SysFont(None, 18)
            text = font18.render("Déplacements :",True,(0,0,0))
            fenetre. blit(text, (300,330))
            controls = pygame.image.load("keypad.png").convert_alpha()
            controls = pygame.transform.scale(controls, (90,80))
            fenetre.blit(controls, (340,350))
            disp_text("Appuyez sur échap pour quitter le",390,445)
            disp_text("jeu",390,460)

            #Explication au joueur comment sortir des menus
            font15 = pygame.font.SysFont(None, 15)
            text = font15.render(("Appuyez sur espace pour retourner"),True,(0,0,0))
            fenetre.blit(text,(305,475))
            pygame.display.flip()

        if menu == 3:
            #Carré est déssiné pour donner les informations au joueur
            pygame.draw.rect(fenetre,(0,255,0),(290,290,200,200))
            pygame.draw.rect(fenetre,(0,200,0),(290,290,200,200),5)

            #Mise en place du curseur pour modifier la vitesse du serpent
            disp_text("Vitesse de déplacement :",390,320)
            pygame.draw.rect(fenetre,(235,51,36),(320,350,size_barre,15))
            pygame.draw.rect(fenetre,(0,200,0),(320,350,140,15),3)
            disp_text("Appuez sur <- et -> pour modifier",390,380)
            disp_text("Appuyez sur R pour les",390,430)
            disp_text("paramètres initiaux",390,450)
            font15 = pygame.font.SysFont(None, 15)

            #Explication au joueur comment sortir des menus
            text = font15.render(("Appuyez sur espace pour retourner"),True,(0,0,0))
            fenetre.blit(text,(305,475))
            pygame.display.flip()

        if menu == 4:
            #Carré est déssiné pour donner les informations au joueur
            pygame.draw.rect(fenetre,(0,255,0),(290,290,200,200))
            pygame.draw.rect(fenetre,(0,200,0),(290,290,200,200),5)

            #Représentation des informations
            disp_text("Crédits:",390,310)
            disp_text("Image tête du serpent: MegaPixel",390,350)
            disp_text("Bruit du mouvement: Jeckkech",390,380)
            disp_text("Bruit de collision: ProjectsU012",390,410)
            disp_text("Voir README.md pour les liens",390,440)

            #Explication au joueur comment sortir des menus
            font15 = pygame.font.SysFont(None, 15)
            text = font15.render(("Appuyez sur espace pour retourner"),True,(0,0,0))
            fenetre.blit(text,(305,475))
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
        for i in range(1,length): #Chargement du corps du serpent
            couverture.blit(corps1, (x[i], y[i]))

        # Modification de la position de la tête du serpent
        if depUp:
            y[0] = y[0] - step #Déplacement de la position de la tête
            fenetre.blit(couverture, (0,0)) #Chargement du fond d'écran, de la tête
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
        if x[0] + 35 > fenetre_rect.right:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if y[0] < fenetre_rect.top:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if y[0] + 35 > fenetre_rect.bottom:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3

        #Chargement du fruit
        fenetre.blit(fruit, position_fruit)

        #Verification de si le serpent touche un fruit
        if collision(x[0], y[0], position_fruit.x, position_fruit.y,35,25):
            position_fruit.x = randint(1,20)*step   #Nouvelles coordonnées du fruit lorsqu'il est "mangé"
            position_fruit.y = randint(1,20)*step
            for j in range(0,length):
            	while collision(position_fruit.x, position_fruit.y, x[j], y[j],35,25):
            		position_fruit.x = randint(1,20)*step   #Nouvelles coordonnées du fruit si les premieres insérés ont les même coordonnées que le corps du serpent
            		position_fruit.y = randint(1,20)*step
            length = length + 2
            score = score + 1

        #Vérification de si la tête du serpent touche un morceau du corps
        
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
        time.sleep (vitesse / 1000.0)

    #Etat de la partie terminée
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
