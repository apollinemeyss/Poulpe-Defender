#!/usr/bin/env python
# -*- coding: utf-8 -*-
from terrain import Terrain
#from poulpe import Poulpe
from score import Score
#from invaders import Invaders
#from menu import Menu
import pygame
import time
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
fond = pygame.image.load("background_espace.png").convert()#On définie l'image background_espace comme fond de l'interface
fenetre.blit(fond, (0,0))

poulpe = pygame.image.load("poulpe.png").convert_alpha()
position_poulpe = poulpe.get_rect()
position_poulpe.center = 320,420 #A posé des problèmes
fenetre.blit(poulpe, (200,300))

pygame.display.flip()



terrain = Terrain()
score = Score('Leo')
score.ajouterPoint()

print(score.recupererPoint())
continuer = 1
pygame.key.set_repeat(1,30)
while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = 0
                if event.type == KEYDOWN:
                        if event.key == K_LEFT:                                 #Lorsque l'on va appuyer sur la flèche de droite
                                position_poulpe = position_poulpe.move(-5,0)      #Le poulpe va se déplacer de 5px vers la droite
                        if event.key == K_RIGHT:                                #Lorsque l'on va appuyer sur la flèche de gauche
                                position_poulpe = position_poulpe.move(5,0)       #Le poulpe va se déplacer de 5px vers la gauche

        fenetre.blit(fond, (0,0))
        fenetre.blit(poulpe, position_poulpe)
        pygame.display.flip()
        time.sleep(1)
