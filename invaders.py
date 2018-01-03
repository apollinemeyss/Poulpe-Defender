#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

# Creation classe invaders
class Invaders:
    # fonction d'initialisation, lancé lors de la création
    def __init__(self,pygame,x,y):
        self.pygame = pygame
        self.invaders = self.pygame.image.load("invaders.png").convert_alpha()#alpha pour enlever la partie blanche autour de l'image 
        self.position = self.invaders.get_rect()
        self.position.center = x,y
        #abscisse = x"
        #ordonnée = y"

    #def deplace(self, dx, dy):"
        #self.x=self.x+dx"
        #self.y=self.y+dy"
        
    def allerAdroite(self):
        self.position = self.position.move(5,0)
        #if x>640:"
           #x=640"
        #if x<0:"
            #x=O"

    def allerAgauche(self):
        self.position = self.position.move(-5,0)

    def getInvaders(self):
        return self.invaders

    def getPosition(self):
        return self.position

    #def getAbscisse(self):"
        #return x"
