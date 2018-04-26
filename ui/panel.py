from display import Face
from manage import MouseObservable
from ui import UIElement, Layout
from display.Effect import Animation
import pygame

class Panel(UIElement):
    def __init__(self):
        UIElement.__init__(self)
        self.addContextListner("size", self.reposition)
        self.layout = Layout()

    def setLayout(self, layout):
        self.layout = layout

    def reposition(self, old, new):
        pass

    def onItemAdded(self, item):
        self.layout.placeElements(self.getSize(), self.getItems())
        pass
