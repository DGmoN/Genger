from display.Effect import Painter
from pygame import draw
from pygame import Surface
class PlainColor(Painter):
    def __init__(self, color=(0,0,0)):
        self.color = color

    def apply(self, surface:Surface):
        surface.fill(self.color)
