#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

# Creation classe terrain
class Poulpe:
    # fonction d'initialisation, lancé lors de la création
    def __init__(self,pygame):
        self.pygame = pygame
        self.poulpe = self.pygame.image.load("poulpe.png").convert_alpha()
        self.position = self.poulpe.get_rect()
        self.position.center = 320,420 #Position initiale du poulpe

    def allerAdroite(self):
        self.position = self.position.move(-5,0)

    def allerAgauche(self):
        self.position = self.position.move(5,0)

    def getPoulpe(self):
        return self.poulpe

    def getPosition(self):
        return self.position
