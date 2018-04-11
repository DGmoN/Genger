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


class AnimationSprite(Sprite):
    def __init__(self, image, frames):
        Sprite.__init__(self, image)
        self.frames = frames
        self.frame = 0

    def draw_frame(self, frame, surface):
        pass

    def calculateScroll(self, frame, size):
        pass

    def render(self, surface):
        self.draw_frame(self.frame, surface)
        self.frame += 1
