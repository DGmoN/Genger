from ui import UIElement

class SlideBar(UIElement):
    def __init__(self, onChange):
        UIElement.__init__(self)
        self.level = 0.5
        self.focused = False
        self.onChange = onChange

    def render(self, surface):
        UIElement.render(self, surface)
        from pygame import draw
        w, h = self.size
        draw.rect(surface, (255,255,255), (w * self.level, 0, 5, h))

    def onMouseButtonDown(self, event):
        if(event.button == 1):
            self.focused = True
            self.updatePos(event.pos)

    def updatePos(self, pos):
        px, py = pos
        x, y, w, h = self.getAbsoluteRect()
        self.level = (px - x)/w
        self.repaint(self)
        if(self.onChange): self.onChange(self.level)

    def onMouseMove(self, event):
        if(self.focused):
            self.updatePos(event.pos)

    def onMouseLeave(self, event):
        self.focused = False

    def onMouseButtonUp(self, event):
        self.focused = False
