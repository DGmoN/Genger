from ui import Panel

class LinkPanel(Panel):
    def __init__(self):
        Panel.__init__(self)
        self.tile = None
        self.rects = {}

    def render(self, surface):
        Panel.render(self, surface)
        x, y, w, h = self.getBoudingRect()
        blocksize = 20
        from pygame import draw
        draw.rect(surface, (255,255,255),((w-20)/2, (h-20)/2, 20,20))
        if(self.tile):
            from ui import BeatPannel
            x, y = self.tile.gridPos
            mx, my = BeatPannel.tiles
            wq = int(w/4)
            hq = int(h/4)
            if(x != 0):
                draw.line(surface, (255,255,255), (wq*2, hq*2), (wq, hq*2), 2)
                if(self.tile.links["left"]): draw.rect(surface, (255,255,255),(wq-5, (hq*2)-5, 10, 10))
                else: self.rects["left"] = draw.circle(surface, (255,255,255), (wq, hq*2), 5)
            if(y != 0):
                draw.line(surface, (255,255,255), (wq*2, hq*2), (wq*2, hq), 2)
                if(self.tile.links["top"]): draw.rect(surface, (255,255,255),((wq*2)-5, (hq)-5, 10, 10))
                else: self.rects["top"] = draw.circle(surface, (255,255,255), (wq*2, hq), 5)
            if(x != mx-1):
                draw.line(surface, (255,255,255), (wq*2, hq*2), (wq*3, hq*2), 2)
                if(self.tile.links["right"]): draw.rect(surface, (255,255,255),((wq*3)-5, (hq*2)-5, 10, 10))
                else: self.rects["right"] = draw.circle(surface, (255,255,255), (wq*3, hq*2), 5)
            if(y != my-1):
                draw.line(surface, (255,255,255), (wq*2, hq*2), (wq*2, hq*3), 2)
                if(self.tile.links["bottom"]): draw.rect(surface, (255,255,255),((wq*2)-5, (hq*3)-5, 10, 10))
                else: self.rects["bottom"] = draw.circle(surface, (255,255,255), (wq*2, hq*3), 5)

    def setTile(self, tile):
        self.tile = tile
        self.repaint(self)

    def onMouseButtonDown(self, event):
        if(event.button == 1):
            x, y = event.pos
            ax, ay, w,h = self.getAbsoluteRect()
            x -= ax
            y -= ay
            sx, sy = self.tile.gridPos
            from display import Window
            pannel = Window.instance.BeatPannel
            for i, e in self.rects.items():
                if(e.collidepoint((x, y))):
                    print(sx, sy)
                    if(i == "top"):
                        sy -= 1
                    if(i == "bottom"):
                        sy += 1
                    if(i == "left"):
                        sx -= 1
                    if(i == "right"):
                        sx += 1
                    if(self.tile.links[i]):
                        self.tile.links[i] = None
                        self.repaint(self)
                        return
                    tt = pannel.getGridItem((sx, sy))
                    self.tile.links[i] = tt
                    self.repaint(self)
                    return
