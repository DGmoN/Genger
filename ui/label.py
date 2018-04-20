from ui import UIElement

class Label(UIElement):
    def __init__(self, Text=""):
        UIElement.__init__(self)
        self.text = Text

    def setText(self, text):
        self.text = text
        self.repaint(self)

    def getText(self):
        return self.text

    def render(self, surface):
        UIElement.render(self, surface)
        from display import Window
        text = Window.get_font_provider().render(self.text)
        surface.blit(text, (5, 5))
