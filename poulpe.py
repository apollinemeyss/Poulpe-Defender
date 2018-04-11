#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

# Creation classe poulpe
class Poulpe:
    # fonction d'initialisation, lancée lors de la création
    def __init__(self,pygame,x,y):
        self.pygame = pygame
        self.poulpe = self.pygame.image.load("poulpe.png").convert_alpha()
        self.position = self.poulpe.get_rect()
        self.position.center = x,y #Position initiale du poulpe
        

    def allerAdroite(self):
        if (self.position.x + 15  < 750 ) and ( self.position.x + 15 > 0):
            self.position = self.position.move(5,0)


    def allerAgauche(self):
        if (self.position.x - 15 < 750) and ( self.position.x - 15 > 0):
            self.position = self.position.move(-5,0)


    def getPoulpe(self):
        return self.poulpe #on a besoin de return pour pouvoir rappeler l'image dans le main

    def getPosition(self):
        return self.position #pour pouvoir rappeler la position du poulpe (définie ici dans sa classe) dans le main

    def getX(self):
        return self.position.x
    def getY(self):
        return self.position.y

