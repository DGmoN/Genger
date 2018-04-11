from facade import Face
from manage import MouseObservable
from visible import Sprite, Animateable, Image, Animation
import uuid
import pygame
import random

class AA(Sprite):
    def render(self, surface):
        rect = (0, 0, *(surface.get_size()))
        if(self.picture):
            surface.blit(self.picture, (0,0))
        pygame.draw.rect(surface, (100,100,255, 25) , rect)
        pygame.draw.rect(surface, (255,255,255) , rect, 1)

class blip(Animation):
    def __init__(self, duration):
        Animation.__init__(self, duration)
        self.end = (0,0)
        self.start = (0,0)

    def setEnd(self, position):
        self.end = position

    def setStart(self, position):
        self.start = position

    def onStep(self):
        sx, sy = self.start
        ex, ey = self.end
        dx, dy = (ex - sx), (ey - sy)
        nx = int(dx * self.getCompletion()) + sx
        ny = int(dy * self.getCompletion()) + sy
        self.animate.position= (nx, ny)

class ColourChange(Animation):
    def __init__(self, duration, startcolor=(0,0,0), endcolor=(0,0,0)):
        Animation.__init__(self, duration)
        self.startColor = startcolor
        self.endColor = endcolor
        self.currentCollor = self.startColor


    def onComplete(self):
        if self.time >= self.duration:
            self.direction = -1
            self.time = self.duration
        else:
            self.time = 0

    def onStep(self):
        r1, g1, b1 = self.startColor
        r2, g2, b2 = self.endColor
        rd, gd, bd = (r2 - r1), (g2 - g1), (b2 - b1)
        dd = self.getCompletion()
        self.currentCollor = ((int(rd * dd) + r1), (int(gd * dd) + g1), (int(bd * dd) + b1))
        pass

    def applyRender(self, surf):
        if(self.currentCollor):
            surf.fill(self.currentCollor, special_flags=pygame.BLEND_ADD)

class Block(Face, MouseObservable, Animateable):

    def __init__(self):
        MouseObservable.__init__(self)
        Face.__init__(self)
        Animateable.__init__(self)
        self.ColourChange = ColourChange(200, endcolor=(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
        self.ColourChange.loop = True
        self.addAnimation(self.ColourChange)

    def getSurface(self):
        surf = Face.getSurface(self)
        Animateable.render(self, surf)
        return surf

    def render(self, parent):
        Face.render(self, parent)

    def onMove(self, old, new):
        Face.onMove(self, old, new)

    def draw(self):
        Face.draw(self)

    def onMouseEnter(self, event):
        print("entered ", self)
        self.ColourChange.direction = 1
        pass

    def onMouseLeave(self, event):
        print("left ", self)
        pass

    def onAdded(self, old, new):
        new.addObserveable(self)
        pass

    def onMouseButtonUp(self, event):
        print("Button: ", event.button)
        pass
