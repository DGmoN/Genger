import pyglet
from pyglet import window

class Window(window.Window):
    def __init__(self):
        window.Window.__init__(self, 800,600,"Genger")
        self.bash = pyglet.graphics.Batch()
        self.clock = pyglet.clock.get_default()
        self.clock.schedule_interval(self.update, .01)
        from display.Entities import EntityList, EntityGroup
        self.EE = EntityGroup()
        self.EE.addEntity(EntityList.DEFAULT_ENTITY)
        self.EE.addEntity(EntityList.DEFAULT_BORDER_ENTITY)

        self.EE2 = EntityGroup()
        self.EE2.addEntity(EntityList.DEFAULT_ENTITY)
        self.EE2.addEntity(EntityList.DEFAULT_BORDER_ENTITY)
        self.EE2.abs_x = 100
        self.EE2.abs_y = 100

    def on_draw(self, dt=0):
        self.clear()
        self.EE.draw()
        self.EE2.draw()
        self.clock.tick()
        pass

    def update(self, dt):
        self.EE.abs_x += 1
        self.EE2.abs_y += 1
        pass
