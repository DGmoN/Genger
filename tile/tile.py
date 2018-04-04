from __future__ import absolute_import
from facade.facade import Facade
from manage import MouseListner
from visible.sprite import Sprite
import pygame
import uuid

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
        event.object = self
        rect = self.get_rect()
        if(event.type is pygame.MOUSEMOTION):
            self.inside = rect.collidepoint(event.pos)
        if(event.type is pygame.MOUSEBUTTONUP):
            self.focus = self.inside and (event.button == 1)
        if self.focus and (event.type is pygame.MOUSEBUTTONUP):
            self.onClick(event)
        self.draw()

    def onClick(self, event):
        pass
