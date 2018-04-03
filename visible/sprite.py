import pygame
from pygame import Surface

class Sprite:

    def __init__(self):
        self.size = None

    def render(self, surface):
        rect = (0, 0, *(surface.get_size()))
        if self.size:
            rect = (0, 0, *(self.size))
        pygame.draw.rect(surface, (255,255,255) , rect, 2)
