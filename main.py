from visible import Window
import pygame
from manage import Grid
from tile import Tile
from interface import Panel, Button

def test(event):
    event.object.setText("--------------------")
    print(event.object.getText())

window = Window((800, 600))
grid = Grid(10, 10)
panel = Panel()
button = Button(test)
button.position = (0,0)
window.get_itterator().add_item(grid)
window.get_itterator().add_item(panel)

panel.add_item(button)

grid.position = (0,0)
panel.position= (grid.size[0],0)
panel.setSize((800 - grid.size[0], grid.size[1]))


window.run()
