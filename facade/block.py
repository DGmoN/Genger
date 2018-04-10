from facade import Face
from manage import MouseObservable
from visible import Sprite, Animateable, Image, Animation
import uuid
import pygame

class AA(Sprite):
    def render(self, surface):
        rect = (0, 0, *(surface.get_size()))
        if(self.picture):
            surface.blit(self.picture, (0,0))
        pygame.draw.rect(surface, (100,100,255, 25) , rect)
        pygame.draw.rect(surface, (255,255,255) , rect, 1)

class blip(Animation):
    def __init__(self, duration):
        Animation.__init__(self, duration)
        self.end = (0,0)
        self.start = (0,0)

    def setEnd(self, position):
        self.end = position

    def setStart(self, position):
        self.start = position

    def onStep(self):
        sx, sy = self.start
        ex, ey = self.end
        dx, dy = (ex - sx), (ey - sy)
        nx = int(dx * self.getCompletion()) + sx
        ny = int(dy * self.getCompletion()) + sy
        self.animate.position= (nx, ny)

class ColourChange(Animation):
    def __init__(self, duration):
        Animation.__init__(self, duration)
        self.startColor = (255,255,0)
        self.endColor = (0,0,255)
        self.currentCollor = self.startColor

    def onStep(self):
        r1, g1, b1 = self.startColor
        r2, g2, b2 = self.endColor
        rd, gd, bd = (r2 - r1), (g2 - g1), (b2 - b1)
        dd = self.getCompletion()
        self.currentCollor = ((int(rd * dd) + r1), (int(gd * dd) + g1), (int(bd * dd) + b1))
        pass

    def applyRender(self, surf):
        surf.fill(self.currentCollor, special_flags=pygame.BLEND_ADD)

class Block(Face, MouseObservable, Animateable):

    hover_image = uuid.uuid1()

    def __init__(self):
        MouseObservable.__init__(self)
        Face.__init__(self)
        Animateable.__init__(self)
        self.motion = blip(1000)
        self.ColourChange = ColourChange(1000)
        self.motion.setEnd((100,100))
        self.addAnimation(self.motion)
        self.addAnimation(self.ColourChange)

    def createImage(self):
        from visible import Window
        Face.createImage(self)
        hov = Image((200,200))
        hov.addSprite(AA)
        Window.get_image_registry().registerImage(hov, Block.hover_image)
        pass

    def getSurface(self):
        surf = Face.getSurface(self)
        self.ColourChange.applyRender(surf)
        return surf

    def render(self, parent):
        Animateable.render(self)
        Face.render(self, parent)

    def onMove(self, old, new):
        Face.onMove(self, old, new)
        self.motion.setStart(new)

    def draw(self):
        Face.draw(self)
        from visible import Window
        Window.get_image_registry().get_item(Block.hover_image).draw()

    def onMouseEnter(self, event):
        print("entered ", self)
        self.motion.direction = 1
        self.ColourChange.direction = 1
        pass

    def onMouseLeave(self, event):
        print("left ", self)
        self.motion.direction = -1
        self.ColourChange.direction = -1
        pass

    def onAdded(self, old, new):
        new.addObserveable(self)
        pass

    def onMouseButtonUp(self, event):
        print("Button: ", event.button)
        pass
