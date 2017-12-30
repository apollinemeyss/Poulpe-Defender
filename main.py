#!/usr/bin/env python
# -*- coding: utf-8 -*-
from poulpe import Poulpe
from score import Score
from invaders import Invaders
import pygame
import time
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
fond = pygame.image.load("background_espace.png").convert()#On définie l'image background_espace comme fond de l'interface
fenetre.blit(fond, (0,0))

# creation du poulpe en initialisant un objet poulpe depuis la class Poulpe
poulpe = Poulpe(pygame)
fenetre.blit(poulpe.getPoulpe(), (200,300))

# Création de la liste des invaders
list_invaders = []
for i in range(0,10):
    # on fait i*50 pour décaler les monstres
    list_invaders.append(Invaders(pygame,100+i*50,200))
    fenetre.blit(list_invaders[i].getInvaders(), (100,200))

pygame.display.flip() 

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
                            poulpe.allerAdroite()     #Le poulpe va se déplacer de 5px vers la droite
                        if event.key == K_RIGHT:                                #Lorsque l'on va appuyer sur la flèche de gauche
                            poulpe.allerAgauche()       #Le poulpe va se déplacer de 5px vers la gauche
        fenetre.blit(fond, (0,0))
        fenetre.blit(poulpe.getPoulpe(),poulpe.getPosition())

        # on affiche les monstres
        for i in range(0,10):
            fenetre.blit(list_invaders[i].getInvaders(), list_invaders[i].getPosition())
        pygame.display.flip()
