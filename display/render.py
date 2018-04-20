import pygame, sys
from visible import Sprite
from display import Facade, Face
from manage import Itterator, Input, SpriteRegistry, OWindow, Resources
from tools.debug import Debug
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
        from ui import BeatPannel, TileConfigPanel
        self.BeatPannel = BeatPannel()
        self.ConfigPanel = TileConfigPanel()

        self.addItem(self.BeatPannel)
        self.addItem(self.ConfigPanel)

    def get_sprite_registry():
        return Window.instance.resources.sprite_registry

    def get_image_registry():
        return Window.instance.resources.image_regestry

    def get_font_provider():
        return Window.instance.resources.font_provider


    def config(self):
        pygame.init();
        self.clock = pygame.time.Clock()
        self.resources = Resources()
        self.surface = pygame.display.set_mode(self.dimentions)
        self.surface.set_colorkey(Window.transparent)
        self.init()

    def get_itterator(self):
        return self

    def onWindowCloseRequest(self, event):
        self.active = False
        sys.exit()

    def draw_to_screen(facade: Facade):
        facade.paint(Window.instance.surface)

    def render(self):
        Face.render(self, self.surface)

    def repaint(self, dest):
        if(Debug.LOG_REPAINT): print("!", self.surface, self)
        return self.surface.subsurface(self.getBoudingRect())

    def run(self):
        self.config()
        self.active = True;
        self.surface.fill(Window.transparent)
        self.render()
        while(self.active):
            self.update()
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.observe(pygame.event.get())
            Window.last_frame = self.clock.tick(30)
            pygame.display.flip()
