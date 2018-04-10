import pygame
from pygame.locals import*


#creation classe tir
class Tir:
    def __init__(self,pygame,x,y):
        self.pygame = pygame
        self.tir = self.pygame.image.load("tir.png")
        self.position = self.tir.get_rect()
        self.position.center = x,y        
    def monter(self):
        self.position = self.position.move(0,-15)

    def getTir(self):
        return self.tir

    def getPosition(self):
        return self.position

