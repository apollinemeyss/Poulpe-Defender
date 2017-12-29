import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
#Cette variable fenetre va permettre d'ouvrir une fentre de jeu dans la r�solution voulue, en l'occurence 1920 par 1080px en plein �cran.

#Backround de l'image
fond = pygame.image.load("background_espace.png").convert()#On d�finie l'image background_espace comme fond de l'interface
fenetre.blit(fond, (0,0))

#On d�finie la position du poulpe
poulpe = pygame.image.load("poulpe1.png").convert_alpha()
position_poulpe = poulpe.get_rect()
position_poulpe.center = 320,420 #A pos� des probl�mes
#Au lancement du programme, le poulpe va se trouver en position 320,420
fenetre.blit(poulpe, (200,300))

#Rafraichissement de l'�cran
pygame.display.flip() #A pos� des probl�mes


continuer = 1 #Variable qui prend la valeur 1 et qui va permettre de cr�er une boucle pour ne pas que le programme se ferme
#Boucle infinie
pygame.key.set_repeat(1,30)#Lorsque l'on va rest� appuyer sur une touche, le programme r�p�tera l'action touche toutes les 30ms
while continuer:
        for event in pygame.event.get():    #Attente des �v�nements
                if event.type == QUIT:
                        continuer = 0
                if event.type == KEYDOWN:
                        if event.key == K_LEFT:                                 #Lorsque l'on va appuyer sur la fl�che de droite
                                position_poulpe = position_poulpe.move(-5,0)      #Le poulpe va se d�placer de 5px vers la droite
                        if event.key == K_RIGHT:                                #Lorsque l'on va appuyer sur la fl�che de gauche
                                position_poulpe = position_poulpe.move(5,0)       #Le poulpe va se d�placer de 5px vers la gauche
    
        #Re-collage
        fenetre.blit(fond, (0,0))    
        fenetre.blit(poulpe, position_poulpe)
        #Rafraichissement de la position du poulpe
        pygame.display.flip()
