from facade import Face
from manage import MouseObservable
from visible import Animateable
import uuid
import pygame
import random

class Block(Face, MouseObservable, Animateable):

    def __init__(self):
        MouseObservable.__init__(self)
        Face.__init__(self)
        Animateable.__init__(self)

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
        pass

    def onMouseLeave(self, event):
        print("left ", self)
        #self.ColourChange.direction = -1
        pass

    def onAdded(self, old, new):
        new.addObserveable(self)
        pass

    def onMouseButtonUp(self, event):
        print("Button: ", event.button)
        pass
