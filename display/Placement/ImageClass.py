from pygame import Surface
from display import Context
from display.Effect import Painter

class Image:
    def __init__(self, size, blend_flag=None, context=None):
        self.blend_flag = blend_flag
        self.surface = None
        self.linkedImages = []  # linked images
        self.superImage = None  #The parent image
        self.painters = {}
        if not context:
            self.contextData = Context()
            self.contextData.pos = (0,0)
            self.contextData.size = size
        else : self.contextData = context
        self.contextData.addContextListner("pos", self.onPosChange)
        self.contextData.addContextListner("size", self.onSizeChange)


    def getDepth(self):
        if(self.superImage):
            return self.superImage.getDepth() + 1
        return 0

    def getContext(self):
        return self.contextData

    def getImageSize(self):
        return self.size

    def linkImage(self, image):
        if(image not in self.linkedImages):
            self.linkedImages += [image]
            image.superImage = self
        else: print("Image already linked, cannot link again")

    def unlinkImage(self, image):
        if(image in self.linkedImages):
            self.linkedImages.remove(image)
            image.superImage = None
        else: print("Image not linked, cannot unlink")

    def addPainter(self, id, painter:Painter):
        self.painters[id] = painter

    def onSizeChange(self, old, new):
        pass

    def removePainter(self, id):
        del self.painters[id]

    def create_image(self):
        try:
            self.surface = Surface(self.contextData.size).convert_alpha()
        except ValueError as e:
            print(self.contextData.size)
            raise e

    def getSurface(self):
        if(self.contextData.hasChanged):
            self.contextData.clearChange()
        return self.surface

    def blitLayers(self):
        depth = self.getDepth()
        print("-"*depth,"blitting: ",self)
        for e in self.linkedImages:
            self.surface.blit(e.getSurface(), e.getContext().pos)

    def applyPainters(self):
        depth = self.getDepth()
        print("-"*depth,"painting: ",self)
        for i, e in self.painters.items():
            print("-"*(depth+1),"painter: ",i)
            e.contextData = self.contextData
            e.apply(self.surface)

    def onPosChange(self, old, new):
        self.reblit()
        pass

    def reblit(self):
        self.blitLayers()
        if(self.superImage): self.superImage.reblit()

    def repaint(self):
        print("repaint", self)
        self.applyPainters()
        self.reblit()
        pass

    def render(self):
        depth = self.getDepth()
        print("-"*depth,"rendering: ",self)
        self.create_image()
        for e in self.linkedImages:
            e.render()
        self.blitLayers()
        self.applyPainters()
