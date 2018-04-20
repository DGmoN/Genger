from display import Frame
from manage import Itterator
from tools.debug import Debug
from uuid import uuid1
class Facade(Frame):

    Empty = uuid1()

    def __init__(self):
        Frame.__init__(self)
        self.padding = (10,10,10,10)

    def init(self):
        pass

    def repaint(self, dest):
        if(self.parent):
            surface = self.parent.repaint(dest)
            if(Debug.LOG_REPAINT): print("!", surface, self.getBoudingRect(), self)
            if(dest is self):
                try:
                    #print(surface, self)
                    surface = surface.subsurface(self.getBoudingRect())
                    surface.fill((0,0,0,0))
                    dest.render(surface)
                    return
                except ValueError as e:
                    print(">", surface, self.getBoudingRect(), self)
                    raise e
                except AttributeError as a:
                    print(">", self.parent, surface, self.getBoudingRect(), self)
                    raise a
        return surface.subsurface(self.getBoudingRect())

    def onAdded(self, parent):
        pass

    def render(self, surface):
        from pygame import draw
        if(Debug.SHOW_BOUNDING_RECT):
            draw.rect(surface, (255,255,255, 255), surface.get_rect(), 2)
        draw.rect(surface, (100,100,100, 255), surface.get_rect(), 1)


    def paintInternal(self, surface):
        from display import Window
        if(Debug.SHOW_PADDING):
            surface.fill((0,100,0,100))
        else:
            surface.fill(Window.transparent)

    def paintExternal(self, bounds):
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
