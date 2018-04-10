from visible.sprite import Sprite
from pygame import Surface, Rect
from manage.itterator import Itterator
import uuid

def get_subsurface(parent, get):
    x,y,w,h = get
    if(x < 0):
        w += x
        x = 0
    if(y < 0):
        h += y
        y = 0
    return parent.subsurface((x,y,w,h))

class Facade:

    defult_image = None

    def __init__(self):
        from visible import Window
        self.position = (0, 0)
        self.visible = True
        self.size = (100, 100)
        self.image = None
        self.parent = None

    def getAbsolutePosition(self):
        if not (self.parent):
            return self.position
        x1, y1 = self.position
        x2, y2 = self.parent.position
        return (x1 + x2, y1 + y2)

    def getRect(self):
        return Rect((*self.getAbsolutePosition(), *self.size))

    def createImage(self):
        from visible import Window, Image
        img = Image((200,200))
        img.addSprite(Sprite)
        self.image = Window.get_image_registry().registerImage(img, self.image)

    def getImage(self):
        return self.image

    def setPosition(self, pos):
        self.onMove(self.position, pos)
        self.position = pos

    def onMove(self, old, new):
        pass

    def setParent(self, parent):
        self.onAdded(self.parent, parent)
        self.parent = parent

    def onAdded(self, old, new):
        pass

    def setSize(self, size):
        self.onResize(self.size, size)
        self.size = size

    def onResize(self, old, new):
        pass

    def draw(self):
        from visible import Window
        img = Window.get_image_registry().get_item(self.image)
        if img:
            img.draw()

    def render(self, parent: Surface):
        id = self.getImage()
        if(id):
            from visible import Window
            img = Window.get_image_registry().get_item(id)
            parent.blit(img.getSurface(self.size), self.position)


class Face(Facade, Itterator):
    def __init__(self):
        Facade.__init__(self)
        Itterator.__init__(self)
        self.display = None

    def render(self, parent: Surface):
        if(self.image):
            from visible import Window
            img = Window.get_image_registry().get_item(self.getImage())
            img = img.getSurface(self.size)
            self.display = img.copy()
            self.every(self.render_child)
            parent.blit(self.display, self.position)

    def addItem(self, item):
        Itterator.addItem(self, item)
        item.setParent(self)

    def draw(self):
        Facade.draw(self)
        self.every(self.draw_child)

    def createImage(self):
        Facade.createImage(self)
        for item in self.items:
            item.createImage()

    def render_child(self, item, ittr):
        item.render(self.display)

    def draw_child(self, item, ittr):
        item.draw()
