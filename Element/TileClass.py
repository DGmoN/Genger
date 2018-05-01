from display.Entities import EntityGroup, EntityList

class Tile(EntityGroup):
    def __init__(self):
        EntityGroup.__init__(self)
        self.init_context_vars({
            "anchor_x" : 0,
            "anchor_y" : 0,
            "x" : 0,
            "y" : 0,
            "width" : 0,
            "height": 0,
        })

        self.addContextListner("x", self.onXChange)
        self.addContextListner("y", self.onYChange)
        self.addEntity(EntityList.DEFAULT_ENTITY)
        self.addEntity(EntityList.DEFAULT_BORDER_ENTITY)

    def onXChange(self, old, new):
        for e in self.children:
            e.anchor_x = self.anchor_x + new
        pass
    def onYChange(self, old, new):
        for e in self.children:
            e.anchor_y = self.anchor_y + new
        pass
