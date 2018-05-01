from Element import Tile

class LayoutTile(Tile):
    def __init__(self):
        Tile.__init__(self)
        self.anchors = {}
    """
        Anchor format:
            l, b, r, t => all are floats to point relative to parent
    """

    def addChild(self, child, anchors=(0,0,0,0)):
        Tile.addChild(self,child)
        self.anchors[child] = anchors
        self.update_anchors(child)

    def getLayoutFor(self, child):
        return self.anchors[child]

    def setLayoutFor(self, child, anchors):
        self.anchors[child] = anchors
        self.update_anchors(child)

    def update_anchors(self, child):
        l, b, r, t = self.anchors[child]
        X = l * self.width
        Y = b * self.height
        W = (r * self.width)
        H = (t * self.height)
        child.x = int(X)
        child.y = int(Y)
        child.width = int(W)
        child.height = int(H)
