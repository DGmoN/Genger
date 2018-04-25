from display import Face
from display.Placement import Image
from display.Effect import PlainColor
from manage import MouseObservable, KeyboardObserveable
from visible import Animateable, ColourChange
import pygame
class UIElement(Face, MouseObservable, KeyboardObserveable, Animateable):
    def __init__(self):
        MouseObservable.__init__(self)
        Face.__init__(self)
        KeyboardObserveable.__init__(self)
        Animateable.__init__(self)
        self.img = Image(None, context=self)
        self.img.addPainter("Background",PlainColor((100,0,0,100)))

    def linkImages(self, parentImage):
        Face.linkImages(self, parentImage)
        parentImage.linkImage("baseUIImage", self.img)

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

    def onMouseMove(self, event):
        pass

    def onMouseEnter(self, event):
        self.img.getPainter("Background").getContext().color = (100,255,255)

    def onMouseLeave(self, event):
        self.img.getPainter("Background").getContext().color = (100,0,0,100)
        pass
