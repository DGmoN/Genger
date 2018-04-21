from ui import Panel
from ui import Buttons
from ui import LinkPanel
from ui import TextInput

class TileConfigPanel(Panel):
    def __init__(self):
        Panel.__init__(self)
        self.setSize((200,300))
        self.setPosition((600,300))
        self.linker = LinkPanel()
        self.linker.setPosition((5, 75))
        self.linker.setSize((190, 190))
        self.addItem(self.linker)
        self.grabber = Buttons.KeyGrabButton(self.onKeyGrab)
        self.grabber.setPosition((5,5))
        self.grabber.setSize((190, 30))
        self.colour = Buttons.SlideBar(self.setColor)
        self.colour.setPosition((5, 40))
        self.colour.setSize((190, 30))
        self.addItem(self.colour)
        self.addItem(self.grabber)
        self.soundType = TextInput(self.setSound)
        self.soundType.setSize((190, 30))
        self.soundType.setPosition((5, 270))
        self.addItem(self.soundType)
        self.tile = None

    def setSound(self, text):
        if(self.tile):
            self.tile.configSound(text)
        pass

    def inspectTile(self, tile):
        from pygame import Color
        self.grabber.setKey(tile.key)
        self.tile = tile
        h, s, v, a = Color(*self.tile.color).hsva
        self.colour.level = h/100
        self.colour.repaint(self.colour)
        self.linker.setTile(tile)
        if(tile.soundDir): self.soundType.setText(tile.soundDir)
        else: self.soundType.setText("")

    def setColor(self, hue):
        ang = 360 * hue
        r = (abs(min([ang, 180]) - 180) / 180) * 255
        g = 255 - (((abs(ang - 180))/180) * 255)
        b = (abs(max([ang, 180]) - 180) / 180) * 255
        if(self.tile):
            self.tile.setColor((r,g,b))
        pass

    def onKeyGrab(self, key):
        if(self.tile):
            self.tile.key = key
        print(key)
        pass
