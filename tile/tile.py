from facade.facade import Facade
from manage.listener import Listner
from visible.sprite import Sprite
import pygame
import uuid

class ISprite(Sprite):
    def render(self, surface: pygame.Surface):
        rect = (0, 0, *(surface.get_size()))
        if self.size:
            rect = (0, 0, *(self.size))
        pygame.draw.rect(surface, (255,0,0) , rect, 2)

class FSprite(Sprite):
    def render(self, surface: pygame.Surface):
        rect = (0, 0, *(surface.get_size()))
        if self.size:
            rect = (0, 0, *(self.size))
        pygame.draw.rect(surface, (0,255,0) , rect, 2)

class Tile(Facade, Listner):

    idle_sprite = uuid.uuid1()
    hover_sprite = uuid.uuid1()
    focus_sprite = uuid.uuid1()

    def __init__(self):
        Listner.__init__(self, pygame.MOUSEMOTION)
        Listner.__init__(self, pygame.MOUSEBUTTONUP)
        Facade.__init__(self)
        self.inside = False
        self.focus = False

    def handle(self, event):
        rect = self.get_rect()
        self.draw()
        if(event.type is pygame.MOUSEMOTION):
            self.inside = rect.collidepoint(event.pos)
        if(event.type is pygame.MOUSEBUTTONUP):
            self.focus = self.inside and (event.button == 1)


    def create_sprite(self, registry):
        registry.registerSprite(ISprite, Tile.hover_sprite)
        registry.registerSprite(Sprite, Tile.idle_sprite)
        registry.registerSprite(FSprite, Tile.focus_sprite)

    def get_sprite(self):
        if(self.focus):
            return Tile.focus_sprite
        if(self.inside):
            return Tile.hover_sprite
        return Tile.idle_sprite
