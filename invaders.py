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

    
