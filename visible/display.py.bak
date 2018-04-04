import pygame
from visible import Sprite
from manage import Itterator, Input, SpriteRegistry
from facade import Facade
class Window(Itterator):

    instance = None
    transparent = (0,0,0)

    def __init__(self, dimentions):
        Itterator.__init__(self)
        Window.instance = self
        self.dimentions = dimentions
        self.active = False
        self.surface = None
        self.input = Input()
        self.sprite_regestry = SpriteRegistry()
        self.font_provider = None

    def get_sprite_registry(self):
        return Window.instance.sprite_regestry

    def draw_item(self, item, ittr):
        item.draw()

    def config(self):
        pygame.init();
        from visible import FontProvider
        self.font_provider = FontProvider()
        self.surface = pygame.display.set_mode(self.dimentions)
        self.every(self.draw_item)

    def handle_events(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT) : self.active = False

    def get_itterator(self):
        return self

    def quit(self, event):
        self.active = False

    def render_item(self, item, ittr):
        item.render_sprite(self.surface)

    def run(self):
        self.config()
        self.active = True;
        while(self.active):
            self.surface.fill(Window.transparent)
            self.input.handle()
            self.every(self.render_item)
            pygame.display.flip()
