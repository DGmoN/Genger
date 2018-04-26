from ui import UIElement
from visible import ImageChange, ImageSequence, RadialGlow, ColourChange
from manage import MouseObservable
from pygame.mixer import Sound
class BeatTile(UIElement, MouseObservable):

    def __init__(self):
        UIElement.__init__(self)
        MouseObservable.__init__(self)
        self.setSize((140,140))
        self.background.color = (200,200,200,255)

    def onMouseEnter(self, event):
        self.background.color = (100,100,100,255)

    def onMouseLeave(self, event):
        self.background.color = (200,200,200,255)

    def onMouseButtonDown(self, event):
        if event.button == 1:
            self.background.color = (150,150,150,255)

    def onMouseButtonUp(self, event):
        self.background.color = (100,100,100,255)
