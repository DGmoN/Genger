from display import Frame
from manage import Itterator
from tools.debug import Debug
from uuid import uuid1
from display.Context import Context
class Facade(Frame, Context):

    Empty = uuid1()

    def __init__(self):
        Frame.__init__(self)
        Context.__init__(self)
        #self.addContextListner("pos", self.onMove)
        self.padding = (10,10,10,10)

    def onMove(self, old, new):
        pass

    def init(self):
        pass

    def update(self):
        pass

class Face(Facade, Itterator):
    def __init__(self):
        Facade.__init__(self)
        Itterator.__init__(self)
        self.renderItems = []
        self.childLayer = None

    def addItem(self, item):
        Itterator.addItem(self, item)
        item.parent = self
        self.renderItems += [item]
        item.onAdded(self)

    def render_child(self, item, ittr):
        csurf = self.childLayer.subsurface(item.getBoudingRect())
        item.render(csurf)

    def update_child(self, item, ittr):
        item.update()

    def init_child(self, item, ittr):
        item.init()

    def init(self):
        Facade.init(self)
        self.every(self.init_child)

    def update(self):
        self.every(self.update_child)

    def render(self, surface):
        from display import Window
        try:
            mys = surface#.subsurface(self.getBoudingRect())
        except ValueError as e:
            print(surface, self.getBoudingRect())
            raise e
        Facade.render(self, mys)
        self.childLayer = mys
        self.every(self.render_child)
