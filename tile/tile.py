from facade.facade import Facade
from manage import MouseListner
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

class Tile(Facade, MouseListner):

    idle_sprite = uuid.uuid1()
    hover_sprite = uuid.uuid1()
    focus_sprite = uuid.uuid1()

    def __init__(self):
        MouseListner.__init__(self)
        Facade.__init__(self)
        self.inside = False
        self.focus = False

    def handle(self, event):
        rect = self.get_rect()
        if(event.type is pygame.MOUSEMOTION):
            self.inside = rect.collidepoint(event.pos)
        if(event.type is pygame.MOUSEBUTTONUP):
            self.focus = self.inside and (event.button == 1)
        self.draw()

    def create_sprite(self, registry):
        registry.registerSprite(Sprite, Tile.hover_sprite, "hover_tile.png")
        registry.registerSprite(Sprite, Tile.idle_sprite, "idle_tile.png")
        registry.registerSprite(Sprite, Tile.focus_sprite, "focus_tile.png")

    def onResize(self, old, new):
        from visible import Window
        Window.instance.get_sprite_registry().get_item(Tile.idle_sprite).setSize(new)
        Window.instance.get_sprite_registry().get_item(Tile.hover_sprite).setSize(new)
        Window.instance.get_sprite_registry().get_item(Tile.focus_sprite).setSize(new)

    def get_sprite(self):
        if(self.focus):
            return Tile.focus_sprite
        if(self.inside):
            return Tile.hover_sprite
        return Tile.idle_sprite
