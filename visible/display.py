import pygame, sys
from visible import Sprite
from manage import Itterator, Input, SpriteRegistry, OWindow, Resources
from facade import Facade, Face

class Window(Face, OWindow):

    instance = None
    transparent = (0,0,0,0)
    last_frame = 0
    frameCount = 0

    def __init__(self, dimentions):
        Face.__init__(self)
        OWindow.__init__(self)
        Window.instance = self
        self.resources = None
        self.dimentions = dimentions
        self.active = False
        self.surface = None
        self.clock = None

    def get_sprite_registry():
        return Window.instance.resources.sprite_registry

    def get_image_registry():
        return Window.instance.resources.image_regestry

    def init_item(self, item, ittr):
        item.createImage()
        item.draw()

    def config(self):
        pygame.init();
        self.clock = pygame.time.Clock()
        self.resources = Resources()
        self.surface = pygame.display.set_mode(self.dimentions)
        self.every(self.init_item)

    def get_itterator(self):
        return self

    def render_item(self, item, ittr):
        item.render(self.surface)

    def onWindowCloseRequest(self, event):
        self.active = False
        sys.exit()



    def run(self):
        self.config()
        self.active = True;
        while(self.active):
            self.surface.fill(Window.transparent)
            self.observe(pygame.event.get())
            self.every(self.render_item)
            Window.last_frame = self.clock.tick()
            pygame.display.flip()
