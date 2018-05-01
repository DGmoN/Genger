import pyglet
from common import Context
class EntityGroup(pyglet.graphics.Group, Context):
    def __init__(self, parent=None):
        pyglet.graphics.Group.__init__(self, parent)
        self.bash = pyglet.graphics.Batch()
        self.entities = {}
        self.children = []
        Context.__init__(self)

    def addEntity(self, entity):
        entity.init_entity_context(self)
        vertex = self.bash.add(entity.vertex_count, entity.target, self, *entity.get_vertex_data(self))
        self.entities[entity] = vertex

    def globalChange(self):
        for e, v in self.entities.items():
            e.update_verticies(v, self)

    def addChild(self, child):
        self.children += [child]
        if("anchor_x" in self.__dict__):
            child.anchor_x = self.anchor_x + self.x
            child.anchor_y = self.anchor_y + self.y
        else:
            child.anchor_x = 0
            child.anchor_y = 0

    def set_state(self):
        pyglet.graphics.Group.set_state(self)
        for ent in self.entities:
            ent.set_context(self)

    def draw(self):
        self.set_state()
        self.bash.draw()
        for e in self.children:
            e.draw()
