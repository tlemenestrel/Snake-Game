# Snake - v0.1
# Ce script est un programme du jeu snake
# License libre CC
# Colin Laganier - Thomas Le Menestrel - 2018.03.27

#Importation des bibliothÃ¨ques nÃ©cessaires
import pygame
from pygame.locals import *
from random import randint

#Initialisation de la bibliothÃ¨que Pygame
pygame.init()

#CrÃ©ation de la fenÃªtre
fenetre = pygame.display.set_mode((700, 700))

#On donne un nom Ã  la fenÃªtre
pygame.display.set_caption("Snake")

#On charge un fond noir avec lequel on remplit la fenÃªtre
couverture = pygame.Surface(fenetre.get_size())
couverture = couverture.convert()
couverture.fill((250, 250, 250))
fenetre.blit(couverture, (0,0))

# On charge un personnage qu'on colle sur la fenÃªtre par dessus le fond noir
Personnage1 = pygame.image.load("F:\ISN\head.png").convert_alpha()
Personnage1 = pygame.transform.scale(Personnage1, (30,30))
fenetre.blit(Personnage1, (0,0))

# On rÃ©cupÃ¨re sa position
position_perso1 = Personnage1.get_rect()

#RafraÃ®chissement de l'Ã©cran
pygame.display.flip()

deplacement = USEREVENT+1
pygame.time.set_timer(deplacement,150)

#Variable qui continue la boucle
continuer = True

runningdroit = False
runningauche = False
runningbas = False
runninghaut = False

#Boucle infinie

while continuer:

    for event in pygame.event.get(): #On parcours la liste de tous les Ã©vÃ©nements reÃ§us

        if event.type == QUIT:
               continuer = False

        if event.type == KEYUP :

            if event.key == K_ESCAPE:

                continuer = False

        # Ensemble des touches qui permettent de dÃ©placer le personnage

        if event.type == KEYDOWN:

            if event.key == K_UP:
                runninghaut = True
                runningbas = False
                runningdroite = False
                runninggauche = False
                while runninghaut == True:
                    for i in range (1,300):
                        position_perso1 = position_perso1.move(0,-1)
                        fenetre.blit(Personnage1, position_perso1)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    if runninghaut == False:
                        break

            elif event.key == K_DOWN:
                runninghaut = False
                runningbas = True
                runningdroite = False
                runninggauche = False
                while runningbas == True:
                    for i in range (1,300):
                         position_perso1 = position_perso1.move(0,1)
                         fenetre.blit(Personnage1, position_perso1)
                         pygame.time.delay(10)
                         pygame.display.flip()
                    if runningbas == False:
                        break

            elif event.key == K_LEFT:
                runninghaut = False
                runningbas = False
                runningdroite = False
                runninggauche = True
                while runninggauche == True:
                    for i in range (1,300):
                        position_perso1 = position_perso1.move(-1,0)
                        fenetre.blit(Personnage1, position_perso1)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    if runninggauche == True:
                        break

            elif event.key == K_RIGHT:
                runninghaut = False
                runningbas = False
                runningdroite = True
                runninggauche = False
                while runningdroit == True:
                    for i in range (1,300):
                        position_perso1 = position_perso1.move(1,0)
                        fenetre.blit(Personnage1, position_perso1)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    if runningdroit == False:
                        break

# On re-colle la fenÃªtre

fenetre.blit(couverture, (0,0))

# On recolle le personnage Ã  sa nouvelle position

fenetre.blit(Personnage1, position_perso1)

pygame.display.flip()
pygame.quit()
