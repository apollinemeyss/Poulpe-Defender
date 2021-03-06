#!/usr/bin/env python
#-*- coding: utf-8 -*-
from poulpe import Poulpe
from invaders import Invaders
from tir import Tir
from tirs_invaders import Tir_Inv
#on a importé tous les objets/classes et leurs fonctions associées 
import pygame
import random
from pygame.locals import *

# Initialisation de pygame et des variables du jeu
#==================================================

#la bibliothèque pygame est importée et initialisée
pygame.init()
clock = pygame.time.Clock()

# Police pour le texte
font = pygame.font.SysFont('Arial', 25)

# Initialisation des images
fenetre = pygame.display.set_mode((800, 600))#on définie la fenetre et ses dimensions
fond = pygame.image.load("background_espace.png")#On définie l'image background_espace comme fond de l'interface
game_over = pygame.image.load("game_over.png")
fond_gagne = pygame.image.load("bravo.png")
tir = pygame.image.load("tir.png")
intro = pygame.image.load("scenario.png")
controles = pygame.image.load("controles.png")

# Initialisation de la musique
pygame.mixer.music.load("musique.wav") #On définie la musique principale du jeu

# Initialisation des booléens pour les boucles
jouer = True
gagner = False
    
# Initialisation de la liste tirs des invaders
list_tirs_invaders = []


# Initialisation de la liste des tirs
list_tirs_poulpe = []

#On introduit une variable score pour ajouter un second but au jeu, il est conservé au cours des parties si on ne perd pas 
score = 0 


#================= Fin initialisation =====================

# fonction pour que l'on puisse rejouer à l'infini, replace les invaders et le poulpe
def reinitialisation():
    
    # On récupère les variables globales
    global jouer
    global gagner
    global list_tirs_poulpe
    global list_invaders
    global list_tirs_invaders
    global poulpe
    global score 

    
    # Initialisation de la liste des invaders
    list_invaders = []

    for i in range(0, 11):
        # on fait i*50 pour décaler les monstres
        list_invaders.append(Invaders(pygame, 100 + i * 50, 300,
                                      "verts"))  # inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y
    for i in range(0, 11):
        # on fait i*50 pour décaler les monstres
        list_invaders.append(Invaders(pygame, 100 + i * 50, 250,
                                      "rouges"))  # inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y
    for i in range(0, 11):
        # on fait i*50 pour décaler les monstres
        list_invaders.append(Invaders(pygame, 100 + i * 50, 200,
                                      "marrons"))  # inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y

    for i in range(0, 11):
        # on fait i*50 pour décaler les monstres
        list_invaders.append(Invaders(pygame, 100 + i * 50, 150,
                                      "bleus"))  # inserer dans la liste(en commençant par la fin)les invaders et leurs coordonnées x,y


    # Création du poulpe en initialisant un objet poulpe depuis la class Poulpe
    poulpe_position_initial_x = 320
    poulpe_position_initial_y = 420
    poulpe = Poulpe(pygame, poulpe_position_initial_x, poulpe_position_initial_y)

    # On remet les booleens a zero
    jouer = True
    gagner = False


# Ajoute un tir du poulpe à la liste des tirs
def ajouter_tir(x, y):
    global list_tirs_poulpe  # à chaque fois on définit les variables communes à toutes les fonctions
    #on ajoute un tir dans la liste, avec les position du poulpe (car doit etre affiché au dessus de lui)
    list_tirs_poulpe.append(Tir(pygame, x + 20, y - 20))  # +20 pour centrer l'image de tir

def ajouter_tir_invaders(x_i, y_i):
    global list_tirs_invaders
    list_tirs_invaders.append(Tir_Inv(pygame, x_i + 20, y_i + 20)) 


# Fonction d'affichage de l'introduction du jeu
def introduction():
    explication = True
    controle = True

    # On récupère les variables globales
    global jouer
    global fond
    global intro

    fenetre.blit(fond, (0,0)) # on colle le fond créé sur la fenetre, en définissant les coordonnées du point de collage(haut gauche)

    # On affiche le panneau explication
    fenetre.blit(intro, (0,0))
    pygame.display.flip()
    while explication and jouer:
        for event in pygame.event.get():
            if event.type == KEYDOWN: 
                if event.key == K_SPACE:  #Si on appuie sur espace:
                       explication = False   #la fenetre se ferme et on passe à la prochaine
                if event.key == QUIT or event.key == K_ESCAPE: #si on clique sur la croix ou si on fait echap :
                        jouer = False  #le jeu se ferme 
        # On récupère les événements 10 fois par seconde, pour éviter de boucler trop rapidement
        clock.tick(10)

    # On affiche la panneau contrôle
    fenetre.blit(controles, (0, 0))
    pygame.display.flip()
    while controle and jouer:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    controle = False
                if event.key == QUIT or event.key == K_ESCAPE:
                        jouer = False

        # On récupère les événements 10 fois par seconde, pour éviter de boucler trop rapidement
        clock.tick(10)

# Affiche le panneau Game Over
def gameOver():
    # On récupère les variables globales
    global jouer
    global score

    #Si game over le score est remis à 0
    score = 0

    afficher_gameover= True
    
    fenetre.blit(game_over, (0, 0))  # on recolle le fond
    pygame.display.flip()
    while afficher_gameover and jouer:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:          
                    jouer = True
                    pygame.mixer.music.play()
                    afficher_gameover = False
                if event.key == QUIT or event.key == K_ESCAPE:
                        pygame.mixer.music.stop()
                        jouer = False

        # On récupère les événements 15 fois par seconde, pour éviter de boucler trop rapidement
        clock.tick(15)

# Affiche le panneau gagné
def gagne():
    # On récupère les variables globales
    global jouer

    afficher_gagne = True
    
    fenetre.blit(fond_gagne, (0, 0))  # on recolle le fond
    pygame.display.flip()
    while afficher_gagne and jouer:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    afficher_gagne = False
                if event.key == QUIT or event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    jouer = False

        # On récupère les événements 15 fois par seconde, pour éviter de boucler trop rapidement
        clock.tick(15)


def collision_tir_poulpe():  # collision entre les tirs des invaders et le poulpe / et le bas de la fenetre

    global list_tirs_invaders
    global poulpe


    position_poulpe = poulpe.getPosition()
    # on teste les positions du poulpe et des tirs
    for i in list_tirs_invaders:
        collision_poulpe = False
        position_tir_inv = i.getPosition()
        if (position_poulpe.top < position_tir_inv.bottom) and (position_poulpe.bottom > position_tir_inv.top):
            if (position_poulpe.right > position_tir_inv.left) and (position_poulpe.left < position_tir_inv.right):
                collision_poulpe = True

        # si le tir est tout en bas on le supprime
        if position_tir_inv.top > 2000:  # j'ai pas trouvé d'autres moyen d'inserer un temps entre chaque tirs 
            list_tirs_invaders.remove(i)

        #si le poulpe est touche, le tir disparait et l'information de la collision est envoyé 
        if collision_poulpe:
            list_tirs_invaders.remove(i)
            return True




def collision_tir_invaders():  # collision entre les tirs du poulpe et les invaders/ et le haut de la fenetre
    global list_tirs_poulpe
    global list_invaders
    global score 

    for i in list_invaders:
        position_invaders = i.getPosition()
        collision_tir = False
        for t in list_tirs_poulpe:
            position_tir = t.getPosition()
            # si le bas de l'alien est plus bas que le haut du tir mais que le tir ne l'a pas encore dépassé -> sur la meme ligne
            if position_invaders.bottom > position_tir.top and position_invaders.top < position_tir.bottom:
                # si la gauche de l'alien est plus a gauche que la droite du tir -> tir pas a gauche de l'alien
                # et que la droite de l'alien est plus a droite que la gauche du tir -> tir pas à droite de l'alien => en collision
                if (position_invaders.left < position_tir.right) and (position_invaders.right > position_tir.left):
                    collision_tir = True

            # si le tir est tout en haut on le supprime
            if position_tir.bottom < 0:
                list_tirs_poulpe.remove(t)

        if collision_tir:
            #fenetre.blit 
            list_invaders.remove(i)
            list_tirs_poulpe.remove(t)
            #si un invader est touché on gagne 100 points
            score += 100

def collision():
    global poulpe
    global list_invaders

    position_poulpe = poulpe.getPosition()
    #pour tous les tirs des invaders, on compare leur position avec celle du poulpe
    for i in list_invaders:
        position_invaders = i.getPosition()
        # Si hors du terrain, trop bas 
        if position_invaders.bottom > 420:
            return True
        if (position_poulpe.top < position_invaders.bottom) and (position_poulpe.bottom > position_invaders.top):
            if (position_poulpe.right > position_invaders.left) and (position_poulpe.left < position_invaders.right):
                return True
        else:
            return False 


# Fonction principale du jeu
def jeu():

    global jouer
    global gagner
    global list_tirs_poulpe
    global list_invaders
    global list_tirs_invaders

    # Réinitialisation des variables de la parties
    vie = 3
    gagner = False
    stop_invaders_a_droite = False
    stop_invaders_a_gauche = True

    while jouer:
        #print ("=======================")
        #print ("Nombre de vie: ", vie)
        #print ("Gagner: ", gagner)
        #print ("Nombre invaders: ", len(list_invaders))
        #print ("Nombre de tirs du poulpe: ", len(list_tirs_poulpe))
        #print ("Nombre de tirs des invaders: ", len(list_tirs_invaders))
        #print ("=======================")

        collision_tir_invaders()
        
        #si le poulpe est touché il perd une vie 
        if collision_tir_poulpe():
            vie -= 1
            
        #si plus de vie ou que les invaders sont trop descendus
        if vie == 0 or collision():
            break # Arrete la boucle

        # Si plus d'invaders le joueur a gagné
        if len(list_invaders) == 0:
            gagner = True
            break # Arrete la boucle

        #tirs des invaders 
        if len(list_tirs_invaders) == 0:  # ne crée un tir que si il n'y a pas déjà un autre tir, niveau facile
            # on prend au hasard un invaders qui lachera un tir
            al = random.randint(0, len(list_invaders)-1)
            invader = list_invaders[al]

            # on recupere les coordonnées de cet invaders pour lui faire créer un tir
            x_invaders = invader.getX()
            y_invaders = invader.getY()
            ajouter_tir_invaders(x_invaders,y_invaders)

        #affichage du fond et du poulpe 
        fenetre.blit(fond, (0, 0))  # on recolle le fond
        fenetre.blit(poulpe.getPoulpe(), poulpe.getPosition())  # on recolle le poulpe a sa nouvelle position

        # Affiche le nombre de vie
        fenetre.blit(font.render('Vie: ' + str(vie), True, (15,183,132)), (10, 5)) #render(text, antialias, color, background=None) -> Surface
        # crée une nouvelle surface sur lequel on affiche le texte      couleur ?

        # Affiche le score 
        fenetre.blit(font.render('Score: ' + str(score), True, (255,0,0)), (10, 35)) #render(text, antialias, color, background=None) -> Surface
        # font.render crée une nouvelle surface sur lequel on affiche le texte 


        # on affiche et on bouge les tirs du poulpe
        for i in range(len(list_tirs_poulpe)):
            fenetre.blit(list_tirs_poulpe[i].getTir(),
                         list_tirs_poulpe[i].getPosition())  # collage de l'image et de la position de chaque tir
            list_tirs_poulpe[i].monter()

        # on affiche et on fait bouger les tirs des invaders
        for i in range(len(list_tirs_invaders)):
            fenetre.blit(list_tirs_invaders[i].getTir(),
                         list_tirs_invaders[i].getPosition())  # collage de l'image et de la position de chaque tir de monstre
            list_tirs_invaders[i].descendre()

        # on affiche les monstres
        for i in range(len(list_invaders)):
            fenetre.blit(list_invaders[i].getInvaders(),
                         list_invaders[i].getPosition())  # collage de l'image et de la position de chaque monstre



        # on fait bouger les monstres
        if not (stop_invaders_a_droite):
            for i in range(len(list_invaders)):
                if not (list_invaders[i].allerAdroite()):
                    stop_invaders_a_droite = True
                    stop_invaders_a_gauche = False
                    for a in range(len(list_invaders)):
                        list_invaders[a].descendre()

        elif not (stop_invaders_a_gauche):
            for i in range(len(list_invaders)):
                if not (list_invaders[i].allerAgauche()):
                    stop_invaders_a_gauche = True
                    stop_invaders_a_droite = False
                    for a in range(len(list_invaders)):
                        list_invaders[a].descendre()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == QUIT or event.key == K_ESCAPE:
                    jouer = False

                if event.key == K_LEFT:  # Lorsque l'on va appuyer sur la flèche de gauche
                    poulpe.allerAgauche()  # Le poulpe va se déplacer de 5px vers la gauche

                if event.key == K_RIGHT:  # Lorsque l'on va appuyer sur la flèche de droite
                    poulpe.allerAdroite()  # Le poulpe va se déplacer de 5px vers la droite

                if event.key == K_SPACE:
                    x = poulpe.getX()
                    y = poulpe.getY()
                    if len(list_tirs_poulpe) == 0: # On autorise un seul tir en même temps au poulpe
                        ajouter_tir(x, y)

        # si on reste appuyer sur gauche ou droite
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            poulpe.allerAgauche()
        if keys[K_RIGHT]:
            poulpe.allerAdroite()

        # On actualise 30 fois par seconde
        clock.tick(30)


#=========================================================================

#On lance l'introduction et la musique avant la boucle principale, histoire qu'elle ne s'arrête pas quand le jeu se relance
introduction()
pygame.mixer.music.play()

# Boucle principale du jeu, on peut rejouer tant qu'on a pas quitté le jeu
while jouer:
    reinitialisation()
    jeu()
    if gagner:
        gagne()
    else:
        gameOver()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == QUIT or event.key == K_ESCAPE:
                jouer = False

    # On récupère les événements 10 fois par seconde, pour éviter de boucler trop rapidement
    clock.tick(10)

pygame.quit()






        
















        
