from display import Frame
from manage import Itterator
from tools.debug import Debug
from display.Context import Context
from pygame import Rect
from display.Placement import Image

class Facade(Frame, Context):

    def __init__(self):
        Frame.__init__(self)
        Context.__init__(self)
        self.absolutePos = (0,0)
        self.addContextListner("pos", self.updateAbsolutePos)
        self.padding = (10,10,10,10)

    def updateAbsolutePos(self, old, new):
        if(self.parent):
            x, y = self.parent.absolutePos
            ix, iy = new
            self.absolutePos = (x + ix, y + iy)
            return
        self.absolutePos = self.pos
        pass

    def getAbsoluteRect(self):
        x, y = self.absolutePos
        w, h = self.size
        return Rect((x,y,w,h))

    def onAdded(self, parent):
        pass

    def linkImages(self, parentImage):
        pass

class Face(Facade, Itterator):
    def __init__(self):
        Facade.__init__(self)
        Itterator.__init__(self)
        self.renderItems = []
        self.childLayer = Image(None, context=self)

    def updateAbsolutePos(self, old, new):
        Facade.updateAbsolutePos(self,old,new)
        self.every(self.updateChildAbsolutePos)

    def updateChildAbsolutePos(self, item, ittr):
        item.updateAbsolutePos(item.pos, item.pos)

    def addItem(self, item):
        Itterator.addItem(self, item)
        item.parent = self
        self.renderItems += [item]
        item.onAdded(self)
        self.onItemAdded(item)

    def onItemAdded(self, item):
        pass

    def linkChildImages(self, item, ittr):
        item.linkImages(self.childLayer)

    def linkImages(self, parentImage):
        Facade.linkImages(self, parentImage)
        parentImage.linkImage("childLayer",self.childLayer)
        self.every(self.linkChildImages)
        pass
