from __future__ import absolute_import
from manage import MouseListner
from tile import Tile
from facade import Face

class Grid(Face):

    tile_size = (50, 50)

    def __init__(self, w, h):
        Face.__init__(self)
        self.grid = {}
        self.size = (w * Grid.tile_size[0], h * Grid.tile_size[1])
<<<<<<< HEAD
        for y in xrange(h):
            for x in xrange(w):
                tile = Hovertile()
=======
        for y in range(h):
            for x in range(w):
                tile = Tile()
>>>>>>> parent of 8202b51... fixed a bug
                tile.position = (x * Grid.tile_size[0], y * Grid.tile_size[1])
                tile.setSize(Grid.tile_size)
                self.add_item(tile)
                self.grid[unicode(x) + u":" + unicode(y)] = tile
                tile.setSize(Grid.tile_size)
                self.add_item(tile)
        pass
