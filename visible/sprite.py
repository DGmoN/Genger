import pygame
from pygame import Surface
import os
class Sprite:

    def __init__(self, image):
        self.size = None
        self.picture = None
        if(image):
            self.picture = pygame.image.load(os.path.abspath("img/" + image))

    def setSize(self, size):
        self.size = size
        if(self.picture):
            self.picture = pygame.transform.scale(self.picture, size)

    def render(self, surface):
        rect = (0, 0, *(surface.get_size()))
        surface.blit(self.picture, (0,0))
        pygame.draw.rect(surface, (255,255,255) , rect, 1)
