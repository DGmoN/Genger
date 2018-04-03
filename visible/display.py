import pygame
from visible.sprite import Sprite
from manage import Itterator, Input, SpriteRegistry
from facade import Facade
class Window:

    instance = None
    sprite_regestry = SpriteRegistry()
    render_itterator = Itterator()

    def __init__(self, dimentions):
        self.dimentions = dimentions
        self.active = False
        self.surface = None
        Window.instance = self
        self.input = Input()

    def init_sprites(self, item, itter):
        item.create_sprite(Window.sprite_regestry)
        item.draw()
        pass

    def get_sprite_registry():
        return Window.instance.sprite_regestry

    def config(self):
        pygame.init();
        self.surface = pygame.display.set_mode(self.dimentions)
        Window.render_itterator.every(self.init_sprites)

    def handle_events(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT) : self.active = False

    def render(self, item : Facade, itter: Itterator):
        item.render_sprite(self.surface)

    def get_itterator(self):
        return Window.render_itterator

    def quit(self, event):
        self.active = False

    def run(self):
        self.config()
        self.active = True;
        while(self.active):
            self.input.handle()
            Window.render_itterator.every(self.render)
            pygame.display.flip()
