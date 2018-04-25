from pygame import Surface
from display.Context import Context
class Painter:
    def __init__(self):
        self.boundImage = None
        self.contextData = Context()

    def getContext(self):
        return self.contextData

    def apply(self, surface:Surface):
        pass
