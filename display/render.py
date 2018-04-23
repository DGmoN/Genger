import pygame, sys
from visible import Sprite
from display import Facade, Face
from display.Effect import PlainColor
from manage import ImageRegistry, OWindow
from display.Placement import Image
from tools.debug import Debug

class Display(Image):

    TRANSPARENT = (0,0,0,0)

    IMAGEREGISTRY = ImageRegistry()

    def create_image(self):
        self.surface = pygame.display.set_mode(self.contextData.size)
        self.surface.set_colorkey(Display.TRANSPARENT)

    def run(self):
        pygame.init()
        Window.instance.linkImages(self)
        self.render()
        while(True):
            Window.instance.observe(pygame.event.get())
            pygame.display.flip()

class Window(OWindow, Face):

    instance = None

    def __init__(self, dimentions):
        OWindow.__init__(self)
        Face.__init__(self)
        self.setSize(dimentions)
        Window.instance = self

    def linkImages(self, parentImage):
        image = Image(None, context=self)
        Display.IMAGEREGISTRY.
        image.addPainter("background",PlainColor((100,100,100,100)))
        parentImage.linkImage(image)
        pass

    def onWindowCloseRequest(self, event):
        sys.exit()
