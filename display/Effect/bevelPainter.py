from display.Effect import Painter
from pygame import draw
from pygame import Surface
class BevelPainter(Painter):
    def __init__(self):
        Painter.__init__(self)
        self.contextData.init_context_vars({
        "depth" : 5
        })

    def apply(self, surface:Surface):
        rect = surface.get_rect()
        draw.lines(surface, (100,100,100), False, [(0,0), rect.topright, rect.bottomright], self.getContext().depth)
        draw.lines(surface, (150,150,150), False, [(0,0), rect.bottomleft, rect.bottomright], self.getContext().depth)
        pass
