from ui import Label
from visible import ColourChange
class TextInput(Label):
    def __init__(self, action=None):
        Label.__init__(self, "")
        self.focused = False
        self.hoverColourChange = ColourChange(200)
        self.addAnimation(self.hoverColourChange)
        self.hoverColourChange.addKeyFrame(0, (0, 0, 0))
        self.hoverColourChange.addKeyFrame(1, (100, 100, 100))
        self.hoverColourChange.circular = True
        self.clean = ""
        self.action = action

    def onMouseEnter(self, event):
        self.hoverColourChange.play(1)

    def onMouseButtonUp(self, event):
        if(event.button == 1):
            self.focused = True
            self.clean = ""
            self.setText("|")
            self.grabEvent()

    def onKeyUp(self, event):
        from pygame import key
        if(self.focused):
            if(key.name(event.key) == "return"):
                self.setText(self.clean)
                self.releaseEvent()
                if(self.action): self.action(self.clean)
                self.focused = False
                return
            if(key.name(event.key) == "backspace"):
                self.clean = self.clean[:-1]
            elif key.name(event.key) == "space":
                self.clean += " "
            else:
                self.clean += key.name(event.key)
            self.setText(self.clean + "|")
