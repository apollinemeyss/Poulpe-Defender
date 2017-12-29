#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Creation classe terrain
class Terrain:
    # fonction d'initialisation, lancé lors de la création
    def __init__(self):
        # taille du terrain verticaln horizontal
        self.size = [600,600]

    def reupererTailleTerrain(self):
        return self.size
