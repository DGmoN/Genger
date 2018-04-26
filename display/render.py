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

    DEBUG_OVERLAY = Image((800,600))

    ANIMATION_CONTEXT = Context()
    CLOCK = pygame.time.Clock()

    def __init__(self, size):
        Image.__init__(self, size)
        Display.ANIMATION_CONTEXT.init_context_vars({
        "lastTick" : 0
        })

    def create_image(self):
        self.surface = pygame.display.set_mode(self.contextData.size)
        self.surface.set_colorkey(Display.TRANSPARENT)
        self.paintSurface = self.surface.copy()

    def run(self):
        pygame.init()
        Window.instance.linkImages(self)
        self.dumpRenderTree()
        self.render()
        while(True):
            Window.instance.observe(pygame.event.get())
            self.maintain()
            pygame.display.flip()
            Display.ANIMATION_CONTEXT.lastTick = Display.CLOCK.tick()
            pygame.display.set_caption(str(Display.CLOCK.get_fps()))

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
        #self.img.getRootImage().getLinkedImage("debugOverlay").getPainter("Text").getContext().text = str(event.pos)

    def linkImages(self, parentImage):
        image = Image(None, context=self)
        self.img = image
        image.addPainter("background",PlainColor((100,100,100,100)))
        parentImage.linkImage('WindowBackground', self.img)
        Face.linkImages(self, parentImage)
        pass

    def addItem(self, item):
        Face.addItem(self, item)
        self.addObserveable(item)

    def onWindowCloseRequest(self, event):
        sys.exit()
