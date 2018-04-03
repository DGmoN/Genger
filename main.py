from visible import Window
import pygame
from manage import Grid
from tile import Tile

window = Window((800, 600))
grid = Grid(10, 10)
grid.position = (0,0)

window.get_itterator().add_item(grid)

window.run()
