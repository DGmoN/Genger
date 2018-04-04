import pygame

class Listner:
    def __init__(self, type):
        from visible import Window
        Window.instance.input.add(type, self.handle)
        print("Listener: ", self)

    def handle(self, event):
        pass

class MouseListner(Listner):
    def __init__(self):
        Listner.__init__(self, pygame.MOUSEMOTION)
        Listner.__init__(self, pygame.MOUSEBUTTONUP)

    def handle(self, event):
        pass
