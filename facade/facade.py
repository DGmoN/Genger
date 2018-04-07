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

    defult_sprite = uuid.uuid1()

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

    def create_sprite(self, registry):
        registry.registerSprite(Sprite, Facade.defult_sprite)

    def get_sprite(self):
        return Facade.defult_sprite

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
        spr = self.get_sprite()
        sprite = Window.instance.sprite_regestry.get_item(spr)
        self.image = Surface(self.size).convert_alpha()
        self.image.fill(Window.transparent)
        if sprite and self.visible:
            sprite.render(surface = self.image)
        print(self, " drew")

    def render_sprite(self, parent: Surface):
        if(self.image):
            parent.blit(self.image, self.position)


class Face(Facade, Itterator):
    def __init__(self):
        Facade.__init__(self)
        Itterator.__init__(self)
        self.display = None

    def render_sprite(self, parent: Surface):
        from pygame import Surface
        from visible import Window
        Facade.render_sprite(self, parent)
        self.display = Surface(self.size).convert_alpha()
        self.display.fill(Window.transparent)
        self.every(self.render_child)
        parent.blit(self.display, self.position)

    def addItem(self, item):
        Itterator.addItem(self, item)
        item.setParent(self)

    def draw(self):
        Facade.draw(self)
        self.every(self.draw_child)

    def render_child(self, item, ittr):
        item.render_sprite(self.display)

    def draw_child(self, item, ittr):
        item.draw()
