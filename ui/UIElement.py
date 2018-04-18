from display import Face
from manage import MouseObservable
from visible import Animateable, Animation
class UIElement(Face, MouseObservable, Animateable):
    def __init__(self):
        MouseObservable.__init__(self)
        Animateable.__init__(self)
        Face.__init__(self)

    def onAdded(self, parent):
        parent.addObserveable(self)

    def onMouseEnter(self, event):
        print("Hello")
