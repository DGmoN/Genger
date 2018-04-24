from display.Placement import Image
from pygame.font import Font
from manage.Files.FileProvider import FileProvider

class Text(Image):
    def __init__(self, size, blend=None,context=None):
        Image.__init__(self,size,blend,context)
        if not('text' in self.contextData.__dict__): self.contextData.text = ""
        self.contextData.addContextListner("text", self.onTextChange)
        self.font = None
        self.text = None

    def onTextChange(self, old, new):
        self.create_text()
        self.reblit()
        pass

    def create_text(self):
        if not (self.font):
            
        self.text = self.font.render(self.contextData.text, True, (255,255,255, 255)).convert_alpha()
        self.contextData.size = self.text.get_size()

    def reblit(self):
        if not(self.surface): return
        self.surface.blit(self.text, self.contextData.absolutePos)
        Image.reblit(self)
