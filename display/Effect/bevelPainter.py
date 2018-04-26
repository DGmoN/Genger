from display.Effect import Painter
from pygame import draw
from pygame import Surface
class BevelPainter(Painter):
    def __init__(self):
        Painter.__init__(self)
        self.init_context_vars({
        "depth" : 5
        })
        self.addContextListner("depth", self.onChange)

    def onChange(self, old, new):
        print("Depth changed")
        self.boundImage.repaint()

    def apply(self, surface:Surface):
        rect = surface.get_rect()
        draw.lines(surface, (150,150,150), False, [(0,0), rect.topright, rect.bottomright], self.depth)
        draw.lines(surface, (0,0,0), False, [(0,0), rect.bottomleft, rect.bottomright], self.depth)
        pass
