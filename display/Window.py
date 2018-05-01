import pyglet
from pyglet import window
from Element.Layout import LayoutTile
from display.Entities import EntityGroup

class Window(window.Window, LayoutTile):
    def __init__(self):
        window.Window.__init__(self, 800,600,"Genger")
        LayoutTile.__init__(self)
        self.width = 800
        self.height = 600
        self.clock = pyglet.clock.get_default()
        self.clock.schedule_interval(self.update, .01)

    def on_draw(self, dt=0):
        self.clear()
        self.draw()
        self.clock.tick()
        pass

    def update(self, dt):

        pass
