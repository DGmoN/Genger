
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

    # The bounding rect describes the surface to be drawn to
    def getBoudingRect(self):
        from pygame import Rect
        if(self.parent):
            containBOunds = self.parent.getBoudingRect()
            x, y, w, h = containBOunds
            X, Y = self.position
            return Rect((x + X, y + Y, *self.size))
        return Rect((*self.position, *self.size))

    # returns a rect within the object, intended to be used as padding
    def getInternalRect(self):
        x, y, w, h = self.getBoudingRect()
        l, t, r, b = self.padding
        from pygame import Rect
        return Rect((x + l, y + t, w - r - l, h - t - b))

    def getPosition(self):
        return self.position

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
        print("-"*count, self.getBoudingRect(), self.getInternalRect())
        return count
