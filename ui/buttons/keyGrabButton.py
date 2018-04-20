from ui import Button

class KeyGrabButton(Button):
    def __init__(self, onset):
        Button.__init__(self, "Not ready", None)
        self.focused = False
        self.lastKey = 0
        self.onSet = onset

    def onKeyDown(self, event):
        if(self.focused):
            self.setKey(event.key)
            self.onSet(event.key)
            self.focused = False

    def setKey(self, inkey):
        from pygame import key
        self.lastKey = inkey
        self.setText("Key: " + key.name(self.lastKey))
        self.releaseEvent()

    def onMouseButtonUp(self, event):
        self.focused = True
        self.grabEvent()
