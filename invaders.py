#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

# Creation classe invaders
class Invaders:
    # fonction d'initialisation, lancé lors de la création
    def __init__(self,pygame,x,y,couleur):
        self.pygame = pygame
        if couleur == "verts":
            self.invaders = self.pygame.image.load("invaders.png").convert_alpha()#alpha pour enlever la partie blanche autour de l'image
        if couleur == "rouges":
            self.invaders = self.pygame.image.load("invaders_rouges.png").convert_alpha()#alpha pour enlever la partie blanche autour de l'image
        if couleur == "marrons":
            self.invaders = self.pygame.image.load("invadermarron.png").convert_alpha()#alpha pour enlever la partie blanche autour de l'image
        if couleur == "bleu":
            self.invaders = self.pygame.image.load("invaderbleu.png").convert_alpha()#alpha pour enlever la partie blanche autour de l'image

        self.position = self.invaders.get_rect()
        self.position.center = x,y # position initial du rectangle
       
        
    def allerAdroite(self):
        if (self.position.x + 15  < 750 ) and ( self.position.x + 15 > 0):
            self.position = self.position.move(5,0)
            return True
        self.position=self.position.move(5,0)
        return False
        

    def allerAgauche(self):
        if (self.position.x - 15 < 750) and ( self.position.x - 15 > 0):
            self.position = self.position.move(-5,0)
            return True
        self.position=self.position.move(-5,0)
        return False
        

    def descendre(self):
        self.position = self.position.move(0,5)

    def getInvaders(self):
        return self.invaders

    def getPosition(self):
        return self.position

    def getX(self):
        return self.position.x

    def getY(self):
        return self.position.y

    def couleur(self):
        return couleur
    
    def meurt(self):
        if couleur == "rouges":
            self.invaders = self.pygame.image.load("invaderrougedetruit.png").convert_alpha()
        if couleur == "verts":
            self.invaders = self.pygame.image.load("invadervertdetruit.png").convert_alpha()
