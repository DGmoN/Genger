from facade import Block
from visible import ColourChange, ImageChange
from visible import RadialGlow, ImageSequence
from manage import KeyboardObserveable
import random
import uuid
class BeatTile(Block, KeyboardObserveable):

    Fade = uuid.uuid1()

    def __init__(self):
        KeyboardObserveable.__init__(self)
        Block.__init__(self)
        self.key = 0
        self.backdrop = ImageChange(1000)
        for i in range(24):
            self.backdrop.addKeyFrame(i/23, i)
        self.addAnimation(self.backdrop)

    def onKeyDown(self, event):
        if(event.key == self.key):
            self.backdrop.play()

    def createImage(self):
        Block.createImage(self)
        from visible import Window
        img = Window.get_image_registry().get_item(BeatTile.Fade)
        if(img):
            self.backdrop.setImage(img)
            return

        img = ImageSequence(self.size)
        img.addSprite(RadialGlow)
        Window.get_image_registry().registerImage(img, BeatTile.Fade)
        self.backdrop.setImage(img)
        img.draw()

    def draw(self):
        Block.draw(self)

    def onMouseButtonUp(self, event):

        if(event.button == 1):
            #self.color.addKeyFrame(0.5, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if not(self.backdrop.running):
                self.backdrop.play()
        if(event.button == 2):
            self.backdrop.stop(True)
