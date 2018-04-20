from ui import Panel
from ui import BeatTile
class BeatPannel(Panel):
    size = (600,600)
    tiles = (5,5)

    def __init__(self):
        Panel.__init__(self)
        self.setSize(BeatPannel.size)
        x, y = BeatPannel.tiles
        width, height = BeatTile.tileSize
        mwidth, mheight = BeatPannel.size
        self.grid = []
        print(self.grid)
        for v in range(y):
            row = []
            for h in range(x):
                hmargin = (((mwidth - (width * x)) / x) *(h + 1)) + (width * h)
                vmargin = (((mheight - (height * y)) / y) * (v + 1)) + (height * v)
                tile = BeatTile()
                tile.setPosition((hmargin, vmargin))
                self.addItem(tile)
                row += [tile]
                tile.gridPos = (h, v)
            self.grid += [row]

    def getGridItem(self, pos):
        x,y = pos
        return self.grid[y][x]
