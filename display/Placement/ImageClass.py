from pygame import Surface
import pygame
from display import Context
from display.Effect import Painter

class Image:
    def __init__(self, size, blend_flag=None, context=None):
        self.blend_flag = blend_flag
        self.surface = None
        self.linkedImages = {}  # linked images
        self.blitOrder = []
        self.superImage = None  #The parent image
        self.painters = {}
        if not context:
            self.contextData = Context()
        else : self.contextData = context
        if 'pos' not in self.contextData.__dict__: self.contextData.__dict__['pos'] = (0,0)
        if 'absolutePos' not in self.contextData.__dict__: self.contextData.__dict__['absolutePos'] = (0,0)
        if 'size' not in self.contextData.__dict__:
            if size:  self.contextData.__dict__['size'] = size
            else:   self.contextData.__dict__['size'] = (0,0)
        self.contextData.addContextListner("pos", self.onPosChange)
        self.contextData.addContextListner("size", self.onSizeChange)

    def getSuperImage(self):
        return self.superImage

    def getRootImage(self):
        if self.superImage:
            return self.superImage.getRootImage()
        return self

    def getDepth(self):
        if(self.superImage):
            return self.superImage.getDepth() + 1
        return 0

    def getContext(self):
        return self.contextData

    def getImageSize(self):
        return self.size

    def linkImage(self, imageID, image):
        if(image not in self.linkedImages):
            self.linkedImages[imageID] = image
            if(imageID not in self.blitOrder):
                self.blitOrder += [imageID]
            image.superImage = self
        else: print("Image already linked, cannot link again")

    def unlinkImage(self, imageID):
        if(imageID in self.linkedImages):
            del self.linkedImages[imageID]
            self.blitOrder.remove(imageID)
            image.superImage = None
        else: print("Image not linked, cannot unlink")

    def getLinkedImage(self, imageID):
        if(imageID in self.linkedImages):
            return self.linkedImages[imageID]

    def addPainter(self, id, painter:Painter):
        self.painters[id] = painter

    def onSizeChange(self, old, new):
        pass

    def removePainter(self, id):
        del self.painters[id]

    def create_image(self):
        try:
            self.surface = Surface(self.contextData.size).convert_alpha()
            self.surface.fill((0,0,0,0))
        except ValueError as e:
            print(self.contextData.size)
            raise e

    def getSurface(self):
        if(self.contextData.hasChanged):
            self.contextData.clearChange()
        return self.surface

    def blitLayers(self):
        if not (pygame.display.get_init()):
            return
        self.surface.fill((0,0,0,0))
        depth = self.getDepth()
        print("-"*depth,"blitting: ",self)
        if not (self.surface): self.create_image()
        for e in self.blitOrder:
            img = self.linkedImages[e]
            if(img.getSurface()):
                self.surface.blit(img.getSurface(), img.getContext().absolutePos)

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
        self.blitLayers()
        self.applyPainters()
        if(self.superImage): self.superImage.reblit()
        pass

    def render(self):
        if not (pygame.display.get_init()):
            return
        depth = self.getDepth()
        print("-"*depth,"rendering: ",self)
        self.create_image()
        for e, i in self.linkedImages.items():
            i.render()
        self.blitLayers()
        self.applyPainters()
