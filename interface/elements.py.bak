from facade import Face
from tile import Tile
from facade import Facade
from pygame.font import Font

class Panel(Face):
    pass

class Button(Tile):

    def __init__(self, action, text="button"):
        Tile.__init__(self)
        self.action = action
        self.text = text

    def onClick(self, event):
        self.action(event)

    def setText(self, text):
        self.text = text;
        self.draw()

    def getText(self):
        return self.text

    def draw(self):
        from visible import Window
        text = Window.instance.font_provider.render(self.text)
        self.setSize(text.get_size())
        Tile.draw(self)
        self.image.blit(text, (0,0))
