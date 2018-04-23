from display.Placement import Image
from pygame import Surface

class ContextImage(Image):
    def __init__(self, size, flags=None):
        Image.__init__(size, flags)
        self.Layers = {}   """a layer has an ID that links it to a surface
                                These surfaces are then collapsed onto the base
                                image when painting"""

    def createLayer(self, id, img:Image):
        if(self.Layers[id]):
            print("Layer already created:",id)
            return
        self.Layers[id] = img

    def destroyLayer(self, id):
        if not (self.Layers[id]):
            print("Layer does not exist:",id)
            return
        del self.Layers[id]

    def getLayer(self, id):
        if not (self.Layers[id]):
            print("Layer does not exist:",id)
            return
        return self.Layers[id]

    def create_image(self):
        Image.create_image(self)
        for i in self.Layers[:]:
            self.Layers[i].create_image()
