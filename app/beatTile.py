from facade import Block
from visible import ColourChange
import random
class BeatTile(Block):
    def __init__(self):
        Block.__init__(self)
        self.color = ColourChange(1000)
        self.color.addKeyFrame(0, (0,0,0))
        self.color.addKeyFrame(1, (255,100,100))
        self.color.loop = True
        self.addAnimation(self.color)

    def onMouseButtonUp(self, event):

        if(event.button == 1):
            #self.color.addKeyFrame(0.5, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if not(self.color.running):
                self.color.play()
        if(event.button == 2):
            self.color.stop(True)
