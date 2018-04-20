from ui import Label, UIElement
from visible import ColourChange
class Button(Label):
    def __init__(self, text="", action=None):
        Label.__init__(self, text)
        self.action = action
        self.hoverColourChange = ColourChange(200)
        self.addAnimation(self.hoverColourChange)
        self.hoverColourChange.addKeyFrame(0, (0, 0, 0))
        self.hoverColourChange.addKeyFrame(1, (100, 100, 100))
        self.hoverColourChange.circular = True

    def setAction(self, action):
        self.action = action

    def onMouseButtonUp(self, event):
        if(event.button == 1 and self.action):
            self.action()

    def onMouseEnter(self, event):
        self.hoverColourChange.play(1)
