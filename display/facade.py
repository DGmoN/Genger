from display import Frame
from manage import Itterator
from tools.debug import Debug
class Facade(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.padding = (10,10,10,10)
        pass

    def onAdded(self, parent):
        pass

    def init(self):
        from display import Window
        Window.draw_to_screen(self)

    def paint(self, surface):
        bounds = surface.subsurface(self.getBoudingRect())
        self.paintBounds(bounds)
        subBounds = surface.subsurface(self.getInternalRect())
        self.paintActive(subBounds)

    def paintActive(self, surface):
        from display import Window
        if(Debug.SHOW_PADDING):
            surface.fill((0,100,0,100))
        else:
            surface.fill(Window.transparent)
        print(self.getInternalRect())

    def repaint(self):
        from display import Window
        Window.draw_to_screen(self)

    def paintBounds(self, bounds):
        from display import Window

        if(Debug.SHOW_PADDING):
            bounds.fill((100,0,0,100))
        else:
            bounds.fill(Window.transparent)

    def update(self):
        pass

class Face(Facade, Itterator):
    def __init__(self):
        Facade.__init__(self)
        Itterator.__init__(self)

    def addItem(self, item):
        Itterator.addItem(self, item)
        item.parent = self
        item.onAdded(self)

    def init_child(self, item, ittr):
        item.init()

    def init(self):
        Facade.init(self)
        self.every(self.init_child)
