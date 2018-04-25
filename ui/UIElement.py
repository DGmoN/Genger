from display import Face
from display.Placement import Image
from display.Effect import BevelPainter, PlainColor
from manage import Observeable
from visible import Animateable, ColourChange
import pygame
class UIElement(Face, Observeable):
    def __init__(self):
        Observeable.__init__(self)
        Face.__init__(self)
        self.backpane = Image(None, context=self)
        self.background = self.backpane.addPainter("backbround",PlainColor((100,100,100,100)))
        self.bevel = self.backpane.addPainter("bevel",BevelPainter())

    def linkImages(self, parentImage):
        parentImage.linkImage(str(self)+"backpane",self.backpane)
        Face.linkImages(self, self.backpane)
        pass

    def addItem(self, item):
        Face.addItem(self, item)
        self.addObserveable(item)
