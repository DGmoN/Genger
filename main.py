from display import Window
import pyglet
from display.Entities import EntityGroup, EntityList
from Element.Layout import LayoutTile
from Element import Tile
window = Window()
tile = LayoutTile()
tile2 = LayoutTile()

window.addChild(tile, (0,0, 1, 0.2))
window.addChild(tile2, (0,0.2, 0.8, 0.8))

pyglet.app.run()
