from display.Effect import Painter
from pygame import draw
from pygame import Surface
class PlainColor(Painter):
    def __init__(self, color=None):
        Painter.__init__(self)
        self.init_context_vars({
            "color" : (0,0,0,0)
        })
        if(color):self.color = color
        self.addContextListner("color", self.colorUpdate)

    def colorUpdate(self, old, new):
        self.boundImage.repaint()

    def apply(self, surface:Surface):
        surface.fill(self.color)
