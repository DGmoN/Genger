import pygame

class Listner:
    def __init__(self, type):
        from visible import Window
        Window.instance.input.add(type, self.handle)

    def handle(self, event):
        pass

class MouseListner(Listner):
    def __init__(self):
        from visible import Window
        Window.instance.input.add(pygame.MOUSEMOTION, self.handle)
        Window.instance.input.add(pygame.MOUSEBUTTONUP, self.handle)

    def handle(self, event):
        pass
