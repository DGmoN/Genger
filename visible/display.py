import pygame, sys
from visible import Sprite
from manage import Itterator, Input, SpriteRegistry, MouseListner, OWindow
from facade import Facade, Face

class Window(Face, OWindow):

    instance = None
    transparent = (0,0,0,0)

    def __init__(self, dimentions):
        Face.__init__(self)
        OWindow.__init__(self)
        Window.instance = self
        self.dimentions = dimentions
        self.active = False
        self.surface = None
        self.sprite_regestry = SpriteRegistry()
        self.font_provider = None

    def get_sprite_registry(self):
        return Window.instance.sprite_regestry

    def init_item(self, item, ittr):
        item.create_sprite(self.get_sprite_registry())
        item.draw()

    def config(self):
        pygame.init();
        from visible import FontProvider
        self.font_provider = FontProvider()
        self.surface = pygame.display.set_mode(self.dimentions)
        self.every(self.init_item)

    def get_itterator(self):
        return self

    def render_item(self, item, ittr):
        item.render_sprite(self.surface)

    def onWindowCloseRequest(self, event):
        sys.exit()

    def run(self):
        self.config()
        self.active = True;
        while(self.active):
            self.surface.fill(Window.transparent)
            self.observe()
            self.every(self.render_item)
            pygame.display.flip()
