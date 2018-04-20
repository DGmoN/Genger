from ui import UIElement
from visible import ImageChange, ImageSequence, RadialGlow, ColourChange
from uuid import uuid1
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
        self.sound = None
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

    def onComplete(self, animation):
        if(animation == self.background):
            for i, a in self.links.items():
                if(a):
                    a.beat()

    def beat(self):
        self.background.play(1)
        self.ColourChange.play(1)

    def onMouseEnter(self, event):
        self.beat()

    def onKeyUp(self, event):
        if(event.key == self.key):
            self.beat()

    def onMouseButtonDown(self, event):
        self.beat()
        from display import Window
        Window.instance.ConfigPanel.inspectTile(self)
