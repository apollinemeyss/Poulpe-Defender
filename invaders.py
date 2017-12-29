#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

# Creation classe terrain
class Invaders:
    # fonction d'initialisation, lancé lors de la création
    def __init__(self,pygame,x,y):
        self.pygame = pygame
        self.invaders = self.pygame.image.load("invaders.png").convert_alpha()
        self.position = self.invaders.get_rect()
        self.position.center = x,y #Position initiale du poulpe

    def allerAdroite(self):
        self.position = self.position.move(-5,0)

    def allerAgauche(self):
        self.position = self.position.move(5,0)

    def getInvaders(self):
        return self.invaders

    def getPosition(self):
        return self.position
