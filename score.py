#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Creation classe terrain
class Score:
    # fonction d'initialisation, lancé lors de la création
    def __init__(self,nom):
        # taille du terrain
        self.score = 0
        self.nom = nom

    # fonction d'ajout d'un point
    def ajouterPoint(self):
        self.score+=1

    # fonction qui renvoi le score
    def recupererPoint(self):
        return self.score


