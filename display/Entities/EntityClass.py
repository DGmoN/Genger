import pyglet

class Entity:
    def __init__(self):
        self.id = 0
        self.target = pyglet.gl.GL_QUADS
        self.vertex_count = 4
        pass

    def init_entity_context(self, context):
        context.init_context_vars({
            "anchor_x" : 0,
            "anchor_y" : 0,
            "x" : 50,
            "y" : 50,
            "width" : 50,
            "height": 50,
            "color" : (255,255,255)
        })
        pass

    def set_context(self, context):

        pass

    def update_verticies(self, vertexlist, context):
        x = context.x + context.anchor_x
        y = context.y + context.anchor_y
        w = context.width
        h = context.height
        vertexlist.vertices = [x, y, x+w, y, x+w,y+h,x, y+h]
        vertexlist.colors = list(context.color)*self.vertex_count

    def get_entity_name(self):
        return "DEFAULT"

    def get_position_vertex(self, context):
        x = context.x + context.anchor_x
        y = context.y + context.anchor_y
        w = context.width
        h = context.height
        return ('v2i/dynamic', (x, y, x+w, y, x+w,y+h,x, y+h))

    def get_colour_vertex(self, context):
        return ('c3B/dynamic', (context.color*self.vertex_count))

    def get_vertex_data(self, context):
        return (self.get_position_vertex(context), self.get_colour_vertex(context))

class BorderEntity(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.target = pyglet.gl.GL_LINES
        self.vertex_count = 8

    def get_entity_name(self):
        return "DEFAULT_BORDERED"

    def get_colour_vertex(self, context):
        return ('c3B', (context.border_color*self.vertex_count))

    def init_entity_context(self, context):
        Entity.init_entity_context(self, context)
        context.init_context_vars({
            "anchor_x" : 0,
            "anchor_y" : 0,
            "x" : 50,
            "y" : 50,
            "width" : 50,
            "height": 50,
            "border_width" : 2,
            "border_color" : (100, 100, 100)
        })
        pass

    def set_context(self, context):
        pyglet.gl.glLineWidth(context.border_width)
        pass

    def update_verticies(self, vertexlist, context):
        x = context.x + context.anchor_x
        y = context.y + context.anchor_y
        w = context.width
        h = context.height
        thick = context.border_width

        vertexlist.vertices = [ x,      y+int(thick/2),      x+w,   y+int(thick/2),
                                x+w - int(thick/2),   y,      x+w-int(thick/2),   y+h,
                                x+w,   y+h-int(thick/2),   x,      y+h-int(thick/2),
                                x + int(thick/2),      y,      x+int(thick/2),   y+h]

    def get_position_vertex(self, context):
        x = context.x + context.anchor_x
        y = context.y + context.anchor_y
        w = context.width
        h = context.height
        thick = context.border_width
        return ('v2i/dynamic', ( x,      y+int(thick/2),      x+w,   y+int(thick/2),
                                x+w - int(thick/2),   y,      x+w-int(thick/2),   y+h,
                                x+w,   y+h-int(thick/2),   x,      y+h-int(thick/2),
                                x + int(thick/2),      y,      x+int(thick/2),   y+h))
