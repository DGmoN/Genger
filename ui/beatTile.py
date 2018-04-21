from ui import UIElement
from visible import ImageChange, ImageSequence, RadialGlow, ColourChange
from uuid import uuid1
from pygame.mixer import Sound
class BeatTile(UIElement):
    tileSize = (100, 100)
    back = uuid1()
    registerd = False

    def __init__(self):
        UIElement.__init__(self)
        self.background = ImageChange(200)
        self.ColourChange = ColourChange(200)
        self.color = (255,0,0)
        self.ColourChange.addKeyFrame(0,(1,1,1))
        self.ColourChange.addKeyFrame(1,self.color)
        self.addAnimation(self.background)
        self.addAnimation(self.ColourChange)
        for i in range(0, 24):
            self.background.addKeyFrame(i/23, i)
        self.background.circular = True
        self.ColourChange.circular = True
        self.setSize(BeatTile.tileSize)
        self.soundDir = None
        self.sound = None
        self.playing = False
        self.key = 0
        self.gridPos = (0,0)
        self.links = {"top":None, "right": None, "bottom": None, "left": None}

    def init(self):
        from display import Window
        if not (BeatTile.registerd):
            img = ImageSequence(BeatTile.tileSize)
            img.addSprite(RadialGlow)
            self.background.setImage(img)
            img.draw()
            Window.get_image_registry().registerImage(img, BeatTile.back)
            BeatTile.registerd = True
        else:
            self.background.setImage(Window.get_image_registry().getItem(BeatTile.back))

    def setColor(self, color):
        self.ColourChange.addKeyFrame(1, color)
        self.beat()

    def configSound(self, dir):
        self.soundDir = dir
        import os
        cwd = os.getcwd() + "/sounds/"+dir+".wav"
        if(os.path.isfile(cwd)):
            self.sound = Sound(cwd)
            self.background.duration = self.sound.get_length() * 1000
            self.ColourChange.duration = self.sound.get_length() * 1000
        else:
            print("File does not exist: ",cwd)
            self.sound = None

    def triggerLinks(self):
        for i, e in self.links.items():
            if(e): e.beat()

    def onComplete(self, animation):
        if(animation == self.background):
            self.triggerLinks()
        pass

    def beat(self):
        if(self.sound):
            self.playing = True
            self.grabEvent()
            self.sound.play()
        self.background.play(1)
        self.ColourChange.play(1)

    def onMouseEnter(self, event):
        self.background.time = 100
        self.ColourChange.play(1)

    def onKeyUp(self, event):
        if(event.key == self.key):
            self.beat()

    def onMouseButtonDown(self, event):
        self.beat()
        from display import Window
        Window.instance.ConfigPanel.inspectTile(self)
