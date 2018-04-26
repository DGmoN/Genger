from display.Effect import Painter
from pygame import Surface
from pygame.font import Font
from manage.Files.FileProvider import FileProvider
class TextPainter(Painter):
    def __init__(self):
        Painter.__init__(self)
        self.font = None
        self.init_context_vars({
            "font_color" : (255,255,255,255),
            "font"       : "arial.ttf",
            "font_size"  : 8,
            "text_pos"   : (0,0),
            "text"       : ""
        })
        self.addContextListner("text", self.textUpdate)
        self.addContextListner("font_color", self.textUpdate)
        self.addContextListner("font", self.textUpdate)
        self.addContextListner("font_size", self.textUpdate)
        self.addContextListner("text_pos", self.textUpdate)

    def textUpdate(self, old, new):
        self.boundImage.repaint()

    def apply(self, surface:Surface):
        if not self.font:
            self.font = Font(FileProvider.getFontFile(self.font), self.font_size)
        sub = self.font.render(self.text, True, self.font_color)
        surface.blit(sub, self.text_pos)
        pass
