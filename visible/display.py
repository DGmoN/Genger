import pygame
from visible import Sprite
from manage import Itterator, Input, SpriteRegistry, MouseListner
from facade import Facade, Face
class Window(Face, Input):

    instance = None
    transparent = (0,0,0,0)

    def __init__(self, dimentions):
        Face.__init__(self)
        Input.__init__(self)
        self.addAction(pygame.QUIT, self.quit)
        self.addActionGroup(Input.EventGroups['mouse'], self.test)
        Window.instance = self
        self.dimentions = dimentions
        self.active = False
        self.surface = None
        self.sprite_regestry = SpriteRegistry()
        self.font_provider = None

    def test(self, event):
        print(event)

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
            self.testEvents()
            self.every(self.render_item)
            pygame.display.flip()
