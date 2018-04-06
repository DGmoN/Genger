import pygame
from manage import Input

class Listner(Input):
    def __init__(self):
        Input.__init__(self)


class MouseListner(Listner):
    def __init__(self):
        Listner.__init__(self)
        self.addAction(pygame.MOUSEMOTION, self.onMouseMove)
        self.addAction(pygame.MOUSEBUTTONUP, self.onMouseButtonUp)

    def onMouseMove(self, event):
        print("Mouse move: ",self)
        pass

    def onMouseButtonUp(self, event):
        print("Mouse button up: ",self)
        pass
