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

    def get_rect(self):
        return Rect((*self.position, *self.size))

    def create_sprite(self, registry):
        registry.add_item(Sprite, Facade.defult_sprite)

    def get_sprite(self):
        return Facade.defult_sprite

    def draw(self):
        spr = self.get_sprite()
        from visible import Window
        sprite = Window.get_sprite_registry().get_item(spr)
        if sprite and self.visible:
            self.image = Surface(self.size)
            sprite.render(self.image)

    def render_sprite(self, parent: Surface):
        parent.blit(self.image, self.position)


class Face(Facade, Itterator):
    def __init__(self):
        Facade.__init__(self)
        Itterator.__init__(self)

    def render_sprite(self, parent: Surface):
        Facade.render_sprite(self, parent)
        self.every(self.render_child)

    def render_child(self, item, itter):
        item.render_sprite(self.image)
