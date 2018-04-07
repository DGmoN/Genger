from facade import Facade
from manage import MouseObservable
from visible import Sprite
import uuid
import pygame

class AA(Sprite):
    def render(self, surface):
        rect = (0, 0, *(surface.get_size()))
        if(self.picture):
            surface.blit(self.picture, (0,0))
        pygame.draw.rect(surface, (255,100,255, 50) , rect)
        pygame.draw.rect(surface, (255,255,255) , rect, 1)


class Block(Facade, MouseObservable):

    hover_sprite = uuid.uuid1()

    def __init__(self):
        MouseObservable.__init__(self)
        Facade.__init__(self)
        pass

    def create_sprite(self, registry):
        Facade.create_sprite(self, registry)
        registry.registerSprite(AA, Block.hover_sprite)

    def get_sprite(self):
        if(self.mouseInside):
            return Block.hover_sprite
        else:
            return Facade.get_sprite(self)

    def onMouseEnter(self, event):
        print("entered ", self)
        self.draw()
        pass

    def onMouseLeave(self, event):
        print("left ", self)
        self.draw()
        pass

    def onAdded(self, old, new):
        new.addObserveable(self)
        pass

    def onMouseMove(self, event):
        #print("moved: ", self)
        pass

    def onMouseButtonUp(self, event):
        print("Button: ", event.button)
        pass
