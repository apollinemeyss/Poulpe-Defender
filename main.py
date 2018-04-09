#!/usr/bin/env python
# -*- coding: utf-8 -*-
from poulpe import Poulpe
from score import Score
from invaders import Invaders
from tir import Tir
#on a importé tous les objets/classes et leurs fonctions associées 
import pygame
import time
from pygame.locals import *

pygame.init()
#la bibliothèque pygame est importée et initialisée

clock = pygame.time.Clock()

fenetre = pygame.display.set_mode((800, 600))#on définie la fenetre et ses dimensions 
fond = pygame.image.load("background_espace.png").convert()#On définie l'image background_espace comme fond de l'interface
game_over = pygame.image.load("game_over.jpg").convert()
tir = pygame.image.load("tir.png").convert()


fenetre.blit(fond, (0,0))#on colle le fond créé sur la fenetre, en définissant les coordonnées du point de collage(haut gauche)

"""intro = pygame.image.load("scenario.png").convert
intr = 1
while intr:
    fenetre.blit(intro, (0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                intr = 0
    pygame.display.flip() #Intro mais qui ne marche pas


controle = pygame.image.load("controle.png").convert
contr = 1
while intr:
    fenetre.blit(contr, (0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                contr = 0
    pygame.display.flip() """




#creation de la liste des tirs
a=0
b=0
list_tirs = []
for t in range (0,5):
    list_tirs.append(Tir(pygame,a,b))
    





# creation du poulpe en initialisant un objet poulpe depuis la class Poulpe
x = 320
y = 420
poulpe = Poulpe(pygame,x,y)
fenetre.blit(poulpe.getPoulpe(), (200,300))


# Création de la liste des invaders

list_invaders_v = [] #verts
for v in range(0,10):
    # on fait i*50 pour décaler les monstres     ?
    list_invaders_v.append(Invaders(pygame,100+v*50,300)) #inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y
    fenetre.blit(list_invaders_v[v].getInvaders(), (100,200)) #on colle les invaders en commençant par x=100,y=200

list_invaders_b = [] #bleus
for b in range(0,10):
    list_invaders_b.append(Invaders(pygame,100+b*50,200)) 
    fenetre.blit(list_invaders_b[b].getInvaders(), (100,100))






tirer=0

"""
position_tir_y=0
position_tir_x=0

#creation du tir


def tir():
    
    _y = poulpe.self.position.y
    print (tir_x)
    print(tir_y)
    tir_x=position_tir_x
    print(tir_x)
    fenetre.blit(tir, x,y)
    pygame.display.flip()
        
        tirer=0
    
    """






def collision():
    position_poulpe = poulpe.getPosition()
    for i in list_invaders:
        position_invaders = i.getPosition()
        # Si hors du terrain
        if position_invaders.bottom > 420:
            return True
        if position_invaders.bottom < position_poulpe.top:
            # rectB est au-dessus
            return False
        if position_invaders.left > position_poulpe.right:
            # rectB est à droite
            return False
        if position_invaders.top > position_poulpe.bottom:
            # rectB est en-dessous
            return False
        else:
                # Dans tous les autres cas il y a collision
            return True




pygame.display.flip() #rafraichissment de l'image pour faire apparaitre les invaders, le poulpe et le fond 

#score
#score = Score('Leo')
#score.ajouterPoint()
#print(score.recupererPoint())




#creation  d'un boucle infinie pour que le jeu ne se ferme pas
continuer = 1
pygame.key.set_repeat(1,10) #on defini l'affichage d'une image toutes les 10ms
stop_invaders_a_droite = False
stop_invaders_a_gauche = True
while continuer:
        for event in pygame.event.get():   #on parcours la liste de tous les évènements pouvant être reçus
                if event.type == QUIT:    #si l'évènement est de type QUIT (on clique sur la croix)
                        continuer = 0   #on arrête la boucle
                
                if event.type == KEYDOWN:   #si une touche du clavier est pressée 
                        if event.key == K_LEFT:   #Lorsque l'on va appuyer sur la flèche de gauche
                            poulpe.allerAgauche()       #Le poulpe va se déplacer de 5px vers la gauche

                        if event.key == K_RIGHT:    #Lorsque l'on va appuyer sur la flèche de droite
                            poulpe.allerAdroite()       #Le poulpe va se déplacer de 5px vers la droite

                        if event.key == K_ESCAPE:
                            continuer = 0

                        if event.key == K_SPACE:
                            tirer=1
                            a=poulpe.getX()
                            b=poulpe.getY()
                            #fenetre.blit(tir, (200,300))#NE FONCTIONNE PAS !
                            #print ("encre")
        #pygame.display.flip()

        if tirer==1:
            print ("encre")
            fenetre.blit(list_tirs[t].getTirs(),(a,b))
            tirer = 0 
            """position_tir_x=poulpe.getX()
            position_tir_y=poulpe.getY()
            
            print(position_tir_x)
            print(position_tir_y)
            tir()"""
                                          

        #print (collision())
        if collision():
            fenetre.blit(game_over, (0,0))   #on recolle le fond   

        else:
            
            fenetre.blit(fond, (0,0))   #on recolle le fond   
            fenetre.blit(poulpe.getPoulpe(),poulpe.getPosition())   #on recolle le poulpe a sa nouvelle position 

            # on affiche les monstres
            for i in range(0,10):
                fenetre.blit(list_invaders[i].getInvaders(), list_invaders[i].getPosition())#collage de l'image et de la position de chaque monstre


            #on fait bouger les monstres
            if not(stop_invaders_a_droite):
                for i in range (0,10):
                    if not(list_invaders[i].allerAdroite()):
                        stop_invaders_a_droite = True
                        stop_invaders_a_gauche = False
                        for a in range(0,10):
                            list_invaders[a].descendre()
                    
            elif not(stop_invaders_a_gauche):
                for i in range (0,10):
                    if not(list_invaders[i].allerAgauche()):
                        stop_invaders_a_gauche = True
                        stop_invaders_a_droite = False
                        for a in range(0,10):
                            list_invaders[a].descendre()

        

        pygame.display.flip()
        clock.tick(40)



        
pygame.quit()















        
