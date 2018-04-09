import pygame
from pygame.locals import*


#creation classe tir
class Tir:
    def __init__(self,pygame,x,y):
        self.pygame = pygame
        self.tir = self.pygame.image.load("tir.png")
        self.position = self.tir.get_rect()
        self.position.center = x,y        

def getTirs(self):
    return self.tir
