import pygame, sys
from visible import Sprite
from display import Facade, Face
from display.Effect import PlainColor, TextPainter
from manage import ImageRegistry, OWindow
from display.Placement import Image
from tools.debug import Debug
from display import Context

class Display(Image):

    TRANSPARENT = (0,0,0,0)

    IMAGEREGISTRY = ImageRegistry()

    DEBUG_OVERLAY = Image((300,300))

    DebugContext = Context()

    def create_image(self):
        self.surface = pygame.display.set_mode(self.contextData.size)
        self.surface.set_colorkey(Display.TRANSPARENT)

    def run(self):
        pygame.init()
        Display.DEBUG_OVERLAY.contextData.text = "DEBUG"
        Display.DEBUG_OVERLAY.addPainter("backing",PlainColor((255,255,255,25)))
        Display.DEBUG_OVERLAY.addPainter("Text",TextPainter())
        Display.DEBUG_OVERLAY.contextData.addContextListner("text", self.onTextChange)
        Window.instance.linkImages(self)
        self.linkImage("debugOverlay", Display.DEBUG_OVERLAY)
        self.render()
        while(True):
            Window.instance.observe(pygame.event.get())
            pygame.display.flip()

    def onTextChange(self, old, new):
        Display.DEBUG_OVERLAY.repaint()

class Window(OWindow, Face):

    instance = None

    def __init__(self, dimentions):
        OWindow.__init__(self)
        Face.__init__(self)
        self.setSize(dimentions)
        self.addAction(pygame.MOUSEMOTION, [self.onMouseMove])
        self.img = None
        Window.instance = self

    def onMouseMove(self, event):
        x, y = event.pos
        r = (x/800) * 255
        g = ((x+y)/(800+600)) * 255
        b = (y/600) * 255
        #self.img.getRootImage().getLinkedImage("debugOverlay").getPainter("backing").getContext().color = ((r,g,b, 10))
        self.img.getRootImage().getLinkedImage("debugOverlay").getPainter("Text").getContext().text = str(event.pos)

    def linkImages(self, parentImage):
        Face.linkImages(self, parentImage)
        image = Image(None, context=self)
        self.img = image
        image.addPainter("background",PlainColor((100,100,100,100)))
        parentImage.linkImage('WindowBackground', image)
        pass

    def onWindowCloseRequest(self, event):
        sys.exit()
