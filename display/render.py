import pygame, sys
from visible import Sprite
from display import Facade, Face
from manage import Itterator, Input, SpriteRegistry, OWindow, Resources

class Window(OWindow, Face):

    instance = None
    transparent = (0,0,0,0)
    last_frame = 0
    frameCount = 0

    def __init__(self, dimentions):
        OWindow.__init__(self)
        Face.__init__(self)
        Window.instance = self
        self.setSize(dimentions)
        self.resources = None
        self.dimentions = dimentions
        self.active = False
        self.surface = None
        self.clock = None

    def get_sprite_registry():
        return Window.instance.resources.sprite_registry

    def get_image_registry():
        return Window.instance.resources.image_regestry

    def config(self):
        pygame.init();
        self.clock = pygame.time.Clock()
        self.resources = Resources()
        self.surface = pygame.display.set_mode(self.dimentions)
        self.init()

    def get_itterator(self):
        return self

    def render_item(self, item, ittr):
        item.render(self.surface)

    def onWindowCloseRequest(self, event):
        self.active = False
        sys.exit()

    def draw_to_screen(facade: Facade):
        facade.paint(Window.instance.surface)

    def run(self):
        self.config()
        self.active = True;
        while(self.active):
            self.update()
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.observe(pygame.event.get())
            Window.last_frame = self.clock.tick(30)
            pygame.display.flip()
