import pyglet
from pyglet import window

class Window(window.Window):
    def __init__(self):
        window.Window.__init__(self, 800,600,"Genger")
