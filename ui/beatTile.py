from ui import UIElement
from visible import ImageChange, ImageSequence, RadialGlow
from uuid import uuid1
class BeatTile(UIElement):
    tileSize = (200, 200)
    back = uuid1()
    registerd = False

    def __init__(self):
        UIElement.__init__(self)
        self.background = ImageChange(200)
        self.addAnimation(self.background)
        for i in range(0, 24):
            self.background.addKeyFrame(i/23, i)
        self.background.circular = True

    def init(self):
        if not (BeatTile.registerd):
            from display import Window
            img = ImageSequence(BeatTile.tileSize)
            img.addSprite(RadialGlow)
            self.background.setImage(img)
            img.draw()
            Window.get_image_registry().registerImage(img, BeatTile.back)
            BeatTile.registerd = True
        else:
            self.background.setImage(Window.get_image_registry().getItem(BeatTile.back))

    def onMouseEnter(self, event):
        self.background.play(1)
