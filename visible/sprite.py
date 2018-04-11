import pygame
from pygame import Surface
import os
class Sprite:

    def __init__(self, image):
        self.size = None
        self.picture = None
        self.color = (255,100,100, 25)
        self.frame = 0
        self.frame_limit = 10
        self.mutation = None
        if(image):
            self.picture = pygame.image.load(os.path.abspath("img/" + image))

    def setSize(self, size):
        self.size = size
        if(self.picture):
            self.picture = pygame.transform.scale(self.picture, size)

    def render(self, surface):
        rect = (0, 0, *(surface.get_size()))
        if(self.picture):
            surface.blit(self.picture, (0,0))

        pygame.draw.rect(surface, (1,1,1, 255) , rect)
        pygame.draw.rect(surface, (255,255,255, 255) , rect, 1)
        print("Sprite: ", self)


class RadialGlow(Sprite):
    def __init__(self, image):
        Sprite.__init__(self, None)

    def render(self, surface):
        import math, pygame.gfxdraw
        a, b = surface.get_size()
        mx, my = a/2, b/2
        max = math.sqrt((mx*mx)+(my*my))
        for y in range(b):
            for x in range(a):
                w = x - mx
                h = y - my
                crt = math.sqrt((w*w) + (h*h))
                ax = min([(((crt * (self.mutation)) / max) + (25 / max)) * 255, 255])
                pygame.gfxdraw.pixel(surface, x, y, (255,255,255,ax))
