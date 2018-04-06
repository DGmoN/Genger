from visible import Window
import pygame
from manage import Grid
from tile import Tile, TileContainer
from interface import Panel, Button
from facade import Facade, Face

count = 0

def test(event):
    global count
    event.object.setText(str(count))
    count = count  + 1
    print(event.object.getText())


window = Window((800, 600))

container = Face()
tile = Facade()
tile2 = Facade()
tile.setPosition((0,0))
tile2.setPosition((50,0))
container.addItem(tile)
container.addItem(tile2)
container.setSize((500,500))
window.addItem(container)

window.run()
