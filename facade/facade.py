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
        self.position = (100, 100)
        self.visible = True
        self.size = (100, 100)
        self.image = None
        self.create_sprite(Window.instance.get_sprite_registry())
        self.parent = None

    def getAbsolutePosition(self):
        if not (self.parent):
            return self.position
        x1, y1 = self.position
        x2, y2 = self.parent.position
        return (x1 + x2, y1 + y2)

    def get_rect(self):
        return Rect((*self.getAbsolutePosition(), *self.size))

    def create_sprite(self, registry):
        registry.registerSprite(Sprite, Facade.defult_sprite)

    def get_sprite(self):
        return Facade.defult_sprite

    def setSize(self, size):
        self.onResize(self.size, size)
        self.size = size

    def onResize(self, old, new):
        pass

    def draw(self):
        from visible import Window
        spr = self.get_sprite()
        sprite = Window.instance.sprite_regestry.get_item(spr)
        self.image = Surface(self.size)
        self.image.fill(Window.transparent)
        if sprite and self.visible:
            sprite.render(surface = self.image)

    def render_sprite(self, parent: Surface):
        if(self.image):
            parent.blit(self.image, self.position)


class Face(Facade, Itterator):
    def __init__(self):
        Facade.__init__(self)
        Itterator.__init__(self)
        self.display = None

    def render_sprite(self, parent: Surface):
        Facade.render_sprite(self, parent)
        from pygame import Surface
        self.display = Surface(self.size)
        self.every(self.draw_child)
        parent.blit(self.display, self.position)

    def add_item(self, item):
        Itterator.add_item(self, item)
        item.parent = self

    def draw_child(self, item, ittr):
        item.render_sprite(self.display)
