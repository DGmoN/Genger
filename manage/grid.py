from tile import Tile

class Grid(Tile):

    tile_size = (20, 20)

    def __init__(self, w, h):
        Tile.__init__(self)
        self.size = (w * Grid.tile_size[0], h * Grid.tile_size[1])
        pass
