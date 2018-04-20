from display import Face
from manage import MouseObservable, KeyboardObserveable
from visible import Animateable, ColourChange
import pygame
class UIElement(Face, MouseObservable, KeyboardObserveable, Animateable):
    def __init__(self):
        MouseObservable.__init__(self)
        KeyboardObserveable.__init__(self)
        Animateable.__init__(self)
        Face.__init__(self)

        self.padding = (10,10,10,10)

    def render(self, surface):
        Face.render(self, surface)
        self.paintAnimation(surface)
        pass

    def onStep(self, animation):
        self.repaint(self)
        pass

    def onComplete(self, animation):
        self.repaint(self)

    def update(self):
        Face.update(self)
        self.run()

    def onAdded(self, parent):
        parent.addObserveable(self)

    def onMouseLeave(self, event):
        #self.repaint(self)
        pass
