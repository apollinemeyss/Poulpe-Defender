#!/usr/bin/env python
# -*- coding: utf-8 -*-
from poulpe import Poulpe
from score import Score
from invaders import Invaders
from tir import Tir
from tirs_invaders import Tir_Inv
#on a importé tous les objets/classes et leurs fonctions associées 
import pygame
import random
import time
from pygame.locals import *

pygame.init()
#la bibliothèque pygame est importée et initialisée

clock = pygame.time.Clock()

fenetre = pygame.display.set_mode((800, 600))#on définie la fenetre et ses dimensions 
fond = pygame.image.load("background_espace.png").convert()#On définie l'image background_espace comme fond de l'interface
game_over = pygame.image.load("game_over.png").convert()
fond_gagne = pygame.image.load("bravo.jpg").convert()
tir = pygame.image.load("tir.png").convert()


fenetre.blit(fond, (0,0))#on colle le fond créé sur la fenetre, en définissant les coordonnées du point de collage(haut gauche)

intro = pygame.image.load("scenario.png").convert()
controles = pygame.image.load("controles.png").convert()

intr = 1
while intr:
    fenetre.blit(intro, (0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                intr = 0
    pygame.display.flip() #Intro (scenario)


contr = 1
while contr:
    fenetre.blit(controles, (0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                contr = 0
    pygame.display.flip() #Controles
    
#creation du niveau de vie
vie=3
print ("debut:",vie)

# creation du poulpe en initialisant un objet poulpe depuis la class Poulpe
x = 320
y = 420
poulpe = Poulpe(pygame,x,y)
#fenetre.blit(poulpe.getPoulpe(), (200,300))    ?


# Création de la liste des invaders

list_invaders = [] #verts
for i in range(0,10):
    # on fait i*50 pour décaler les monstres     
    list_invaders.append(Invaders(pygame,100+i*50,300,"verts")) #inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y
for i in range(0,10):
    # on fait i*50 pour décaler les monstres     
    list_invaders.append(Invaders(pygame,100+i*50,200,"rouges")) #inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y



# création liste tir
list_tirs = []
def ajouter_tir(x,y):
    list_tirs.append(Tir(pygame,x+20,y-20)) #+20 pour centrer l'image de tir


#création de la liste tirs des invaders
list_tirs_inv = []
def ajouter_tir_inv(x_i,y_i):
    list_tirs_inv.append(Tir_Inv(pygame, x_i+20, y_i+20))



def collision_tir_invaders(): #collision entre les tirs du poulpe et les invaders/ et le haut de la fenetre
    for i in list_invaders:
        position_invaders = i.getPosition()
        collision_tir = False
        for t in list_tirs:
            position_tir = t.getPosition()
            #si le bas de l'alien est plus bas que le haut du tir mais que le tir ne l'a pas encore dépassé -> sur la meme ligne 
            if position_invaders.bottom > position_tir.top and position_invaders.top < position_tir.bottom:
                #si la gauche de l'alien est plus a gauche que la droite du tir -> tir pas a gauche de l'alien
                #et que la droite de l'alien est plus a droite que la gauche du tir -> tir pas à droite de l'alien => en collision
                if (position_invaders.left < position_tir.right) and (position_invaders.right > position_tir.left):
                    collision_tir = True
                    
            # si le tir est tout en haut on le supprime
            if position_tir.bottom < 0:
                list_tirs.remove(t)
            
        if collision_tir:
            list_invaders.remove(i)
            list_tirs.remove(t)
    
            
def collision_tir_poulpe():  #collision entre les tirs des invaders et le poulpe / et le bas de la fenetre
    collision_poulpe=False
    position_poulpe=poulpe.getPosition()   
    #on teste les positions du poulpe (Poulpe.getPosition()) et des tirs (position_tir_inv)
    for i in list_tirs_inv:
        position_tir_inv = i.getPosition()
        if (position_poulpe.top < position_tir_inv.bottom) and (position_poulpe.bottom > position_tir_inv.top):
            if (position_poulpe.right > position_tir_inv.left) and (position_poulpe.left < position_tir_inv.right):
                collision_poulpe=True
                return True
                
                
        #si le tir est tout en bas on le supprime
        if position_tir_inv.top>600 or collision_poulpe==True: #j'ai pas trouvé d'autres moyen d'inserer un temps entre chaque tirs #3000
            list_tirs_inv.remove(i)
            print collision_poulpe
            print collision_tir_poulpe()

        #if collision_poulpe:
            #list_tirs_inv.remove(i)
            #print list_tirs_inv
        
        
 


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




pygame.display.flip() #rafraichissement de l'image pour faire apparaitre les invaders, le poulpe et le fond 

#score
#score = Score('Leo')
#score.ajouterPoint()
#print(score.recupererPoint())




#creation  d'un boucle infinie pour que le jeu ne se ferme pas
continuer = 1

#pygame.key.set_repeat(1,10) #on defini l'affichage d'une image toutes les 10ms
stop_invaders_a_droite = False
stop_invaders_a_gauche = True
while continuer:
        temps = pygame.time.get_ticks()  #essais sur le temps pour invaders bonus + projectiles espacés + poulpe qui disparait quand il se fait touché 
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
                            x=poulpe.getX()
                            y=poulpe.getY()
                            if len(list_tirs) == 0:
                                ajouter_tir(x,y)

                                
                          
        #pygame.display.flip
        collision_tir_invaders()
        collision_tir_poulpe()
        # si on reste appuyer sur gauche ou droite        
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            poulpe.allerAgauche()
        if keys[K_RIGHT]:
            poulpe.allerAdroite()
    

                    
        if collision() or vie==0:
            fenetre.blit(game_over, (0,0))#on recolle le fond
            print vie

        elif len(list_invaders) == 0:
            fenetre.blit(fond_gagne, (0,0))   #on recolle le fond
            
        else:
            
            fenetre.blit(fond, (0,0))   #on recolle le fond   
            fenetre.blit(poulpe.getPoulpe(),poulpe.getPosition())   #on recolle le poulpe a sa nouvelle position 

            # on affiche les monstres
            for i in range(len(list_invaders)):
                fenetre.blit(list_invaders[i].getInvaders(), list_invaders[i].getPosition())#collage de l'image et de la position de chaque monstre

            # on affiche les tirs
            for i in range(len(list_tirs)):
                fenetre.blit(list_tirs[i].getTir(),list_tirs[i].getPosition())  # collage de l'image et de la position de chaque tir

            # on affiche les tirs des invaders
            for i in range(len(list_tirs_inv)):
                fenetre.blit(list_tirs_inv[i].getTir(),list_tirs_inv[i].getPosition())  # collage de l'image et de la position de chaque tir

            #on fait bouger les monstres
            if not(stop_invaders_a_droite):
                for i in range (len(list_invaders)):
                    if not(list_invaders[i].allerAdroite()):
                        stop_invaders_a_droite = True
                        stop_invaders_a_gauche = False
                        for a in range(len(list_invaders)):
                            list_invaders[a].descendre()
                    
            elif not(stop_invaders_a_gauche):
                for i in range (len(list_invaders)):
                    if not(list_invaders[i].allerAgauche()):
                        stop_invaders_a_gauche = True
                        stop_invaders_a_droite = False
                        for a in range(len(list_invaders)):
                            list_invaders[a].descendre()

        
            # on fait bouger les tirs
            for i in range(len(list_tirs)):
                list_tirs[i].monter()

            #on prend au hasard un invaders qui lachera un tir
            h = random.randint(0, len(list_invaders) - 1)  
            invader = list_invaders[h]

            #on recupere les coordonnées de cet invaders pour lui faire créer un tir 
            x_i = invader.getX()
            y_i = invader.getY()
            
            if len (list_tirs_inv) == 0: #ne crée un tir que si il n'y a pas déjà un autre tir, niveau facile
                ajouter_tir_inv (x_i,y_i)
            
            #on fait bouger les tirs
            for i in range(len(list_tirs_inv)):
                list_tirs_inv[i].descendre()

            #si le poulpe est touché par un tir, il perd une vie 
            if collision_tir_poulpe():
                vie = vie-1
                print vie 
                                 
                        

                
                
        pygame.display.flip()
        clock.tick(30)



        
pygame.quit()















        
