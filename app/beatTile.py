from facade import Block
from visible import ColourChange, ImageChange
from visible import RadialGlow, ImageSequence
import random
import uuid
class BeatTile(Block):

    Fade = uuid.uuid1()

    def __init__(self):
        Block.__init__(self)
        self.color = ColourChange(2000)
        self.color.addKeyFrame(0, (0,0,0))
        self.color.addKeyFrame(0.5, (255,100,100))
        self.color.addKeyFrame(1, (0,0,0))
        self.backdrop = ImageChange(1000)
        self.backdrop.loop = True
        self.color.loop = True
        for i in range(60):
            self.backdrop.addKeyFrame(i/59, i)

        self.addAnimation(self.backdrop)
        self.addAnimation(self.color)

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
            if not(self.color.running):
                self.color.play()
            self.backdrop.play()
        if(event.button == 2):
            self.color.stop(True)
