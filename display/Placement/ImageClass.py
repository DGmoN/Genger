from pygame import Surface
import pygame
from display import Context
from display.Effect import Painter

class Image:
    def __init__(self, size=(0,0), blend_flag=None, context=None):
        self.blend_flag = blend_flag
        self.surface = None
        self.paintSurface = None
        self.linkedImages = {}  # linked images
        self.blitOrder = []
        self.superImage = None  #The parent image
        self.painters = {}
        if not context:
            self.contextData = Context()
        else : self.contextData = context
        self.contextData.init_context_vars({
            "pos" : (0,0),
            "absolutePos" : (0,0),
            "size" : size,
            "scroll": (0,0)
        })
        self.contextData.addContextListner("pos", self.onPosChange)
        self.contextData.addContextListner("size", self.onSizeChange)
        self.queReblit = True

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

    def dumpRenderTree(self):
        depth = self.getDepth()
        for e in self.blitOrder:
            print(depth * "=", e)
            self.linkedImages[e].dumpRenderTree()

    def getContext(self):
        return self.contextData

    def getImageSize(self):
        return self.size

    def linkImage(self, imageID, image):
        if(image not in self.linkedImages):
            self.linkedImages[imageID] = image
            print(self.getDepth()*"~", self)
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
        painter.boundImage = self
        return painter

    def getPainter(self, id):
        if(id in self.painters):
            return self.painters[id]

    def onSizeChange(self, old, new):
        pass

    def removePainter(self, id):
        del self.painters[id]

    def create_image(self):
        try:
            self.surface = Surface(self.contextData.size).convert_alpha()
            self.surface.fill((0,0,0,0))
            self.paintSurface = self.surface.copy()
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

        if not (self.queReblit): return
        #depth = self.getDepth()
        #print("-"*depth,"blitting: ",self)
        if not (self.surface): self.create_image()
        self.surface.fill((0,0,0,0))
        self.surface.blit(self.paintSurface, (0,0))
        for e in self.blitOrder:
            img = self.linkedImages[e]
            if(img.getSurface()):
                self.surface.blit(img.getSurface(), img.getContext().absolutePos)
        self.queReblit = False

    def applyPainters(self):
        #depth = self.getDepth()
        #print("-"*depth,"painting: ",self)
        self.paintSurface.fill((0,0,0,0))
        for i, e in self.painters.items():
            #print("-"*(depth+1),"painter: ",i)
            e.apply(self.paintSurface)

    def onPosChange(self, old, new):
        self.reblit()
        pass

    def reblit(self):
        self.queReblit = True
        if(self.superImage): self.superImage.reblit()

    def repaint(self):
        #print("repaint", self)
        if not(self.surface): return
        self.applyPainters()
        self.reblit()
        pass

    def render(self):
        if not (pygame.display.get_init()):
            return
        #depth = self.getDepth()
        #print("-"*depth,"rendering: ",self.contextData)
        self.create_image()
        self.applyPainters()
        for e, i in self.linkedImages.items():
            i.render()
        self.blitLayers()

    def maintain(self):
        for e, i in self.linkedImages.items():
            if(i.queReblit):
                i.maintain()
        self.blitLayers()
