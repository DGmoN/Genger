from pygame import Surface
from display.Context import Context
class Painter(Context):
    def __init__(self):
        Context.__init__(self)
        self.boundImage = None

    def apply(self, surface:Surface):
        pass
