
"""
A Frame is meant as a descrition of an object in an area.
A Frame has 4 base values
    Width
    Height
    X position
    Y position
"""

class Frame:
    def __init__(self):
        self.position = (0,0)
        self.size = (0,0)
        self.parent = None

    def getAbsoluteRect(self):
        from pygame import Rect
        if(self.parent):
            containBOunds = self.parent.getAbsoluteRect()
            x, y, w, h = containBOunds
            X, Y = self.position
            return Rect((x + X, y + Y, *self.size))
        return self.getBoudingRect()


    # The bounding rect describes the surface to be drawn to
    def getBoudingRect(self):
        from pygame import Rect
        return Rect((*self.position, *self.size))

    def getPosition(self):
        return self.position

    def setPosition(self, pos):
        self.position = pos

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getX(self):
        x, y = self.position
        return x

    def getY(self):
        x, y = self.position
        return y

    def getWidth(self):
        w, h = self.size
        return w

    def getHeight(self):
        w, h = self.size
        return h

    def treePos(self):
        count = 0
        if(self.parent):
            count = self.parent.treePos() + 1
        print("-"*count, self.getAbsoluteRect(), self)
        return count
