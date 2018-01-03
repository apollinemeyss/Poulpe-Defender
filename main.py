#!/usr/bin/env python
# -*- coding: utf-8 -*-
from poulpe import Poulpe
from score import Score
from invaders import Invaders
#on a importé tous les objets/classes et leurs fonctions associées 
import pygame
import time
from pygame.locals import *

pygame.init()
#la bibliothèque pygame est importée et initialisée

clock = pygame.time.Clock()

fenetre = pygame.display.set_mode((640, 480), RESIZABLE)#on définie la fenetre et ses dimensions 
fond = pygame.image.load("background_espace.png").convert()#On définie l'image background_espace comme fond de l'interface
fenetre.blit(fond, (0,0))#on colle le fond créé sur la fenetre, en définissant les coordonnées du point de collage(haut gauche)

# creation du poulpe en initialisant un objet poulpe depuis la class Poulpe
poulpe = Poulpe(pygame)
fenetre.blit(poulpe.getPoulpe(), (200,300))

# Création de la liste des invaders
list_invaders = []
for i in range(0,10):
    # on fait i*50 pour décaler les monstres
    list_invaders.append(Invaders(pygame,100+i*50,200)) #inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y
    fenetre.blit(list_invaders[i].getInvaders(), (100,200)) #on colle les invaders en commençant par x=100,y=200

pygame.display.flip() #rafraichissment de l'image pour faire apparaitre les invaders, le poulpe et le fond 

score = Score('Leo')
score.ajouterPoint()
print(score.recupererPoint())

#creation  d'un boucle infinie pour que le jeu ne se ferme pas
continuer = 1
pygame.key.set_repeat(1,30) #on defini l'affichage d'une image toutes les 30ms
while continuer:
        for event in pygame.event.get():   #on parcours la liste de tous les évènements pouvant être reçus
                if event.type == QUIT:    #si l'évènement est de type QUIT (on clique sur la croix)
                        continuer = 0   #on arrête la boucle 
                if event.type == KEYDOWN:   #si une touche du clavier est pressée 
                        if event.key == K_LEFT:   #Lorsque l'on va appuyer sur la flèche de droite
                            poulpe.allerAdroite()       #Le poulpe va se déplacer de 5px vers la droite
                        if event.key == K_RIGHT:    #Lorsque l'on va appuyer sur la flèche de gauche
                            poulpe.allerAgauche()       #Le poulpe va se déplacer de 5px vers la gauche

        fenetre.blit(fond, (0,0))   #on recolle le fond   
        fenetre.blit(poulpe.getPoulpe(),poulpe.getPosition())   #on recolle le poulpe a sa nouvelle position 

        # on affiche les monstres
        for i in range(0,10):
            fenetre.blit(list_invaders[i].getInvaders(), list_invaders[i].getPosition())#collage de l'image et de la position de chaque monstre
        pygame.display.flip()#rafraichissement de l'écran

        #on fait bouger les monstres 
        #while getPosition(list_invaders[9])!= 150,300:"
        for i in range (0,10):
            list_invaders[i].allerAdroite()
        fenetre.blit(list_invaders[i].getInvaders(), list_invaders[i].getPosition())
        pygame.display.flip()
        clock.tick(20)
        #pygame.time.delay(100)"




        
