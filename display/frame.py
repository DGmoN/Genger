
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
        self.__dict__['pos'] = (0,0)
        self.__dict__['size'] = (0,0)
        self.__dict__['parent'] = None

    def getAbsoluteRect(self):
        from pygame import Rect
        if(self.parent):
            containBOunds = self.parent.getAbsoluteRect()
            x, y, w, h = containBOunds
            X, Y = self.position
            a, b = self.size
            return Rect((x + X, y + Y, a, b))
        return self.getBoudingRect()


    # The bounding rect describes the surface to be drawn to
    def getBoudingRect(self):
        from pygame import Rect
        x, y = self.getPosition()
        w, h = self.getSize()
        return Rect((x, y, w, h))

    def getPosition(self):
        return self.pos

    def setPosition(self, pos):
        self.pos = pos

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getX(self):
        x, y = self.pos
        return x

    def getY(self):
        x, y = self.pos
        return y

    def setX(self, x):
        self.pos = (x, self.getY())

    def setY(self, y):
        self.pos = (self.getX(), y)

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
