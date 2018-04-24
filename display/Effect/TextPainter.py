from display.Effect import Painter
from pygame import Surface
from pygame.font import Font
from manage.Files.FileProvider import FileProvider
class TextPainter(Painter):
    def __init__(self):
        Painter.__init__(self)
        self.font = None

    def apply(self, surface:Surface):
        if "text" in self.contextData.__dict__:
            if not self.font:
                font = "arial.ttf"
                if "font" in self.contextData.__dict__: font = self.contextData.font
                font_size = 8
                if "font_size" in self.contextData.__dict__: font_size = self.contextData.font_size
                self.font = Font(FileProvider.getFontFile(font), font_size)
            color = (255,255,255)
            if "font_color" in self.contextData.__dict__: color = self.contextData.font_color
            sub = self.font.render(self.contextData.text, True, color)
            textpos = (0,0)
            if "text_pos" in self.contextData.__dict__: textpos = self.contextData.text_pos
            surface.blit(sub, textpos)
        pass
