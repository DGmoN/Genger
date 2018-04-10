from pygame import Surface

class Image:
    def __init__(self, size):
        self.size = size
        self.sprites = []
        self.surface = Surface(size).convert_alpha()

    def addSprite(self, spriteClass):
        from visible import Window
        import uuid
        id = uuid.uuid1()
        Window.get_sprite_registry().registerSprite(spriteClass, id)
        self.sprites += [id]

    def draw(self):
        from visible import Window
        self.surface.fill(Window.transparent)
        for e in self.sprites:
            sprite = Window.get_sprite_registry().get_item(e)
            sprite.render(self.surface)
        print("drew: ", self)

    def getSurface(self, size=None):
        ret = self.surface
        if(size):
            from pygame import transform
            ret = transform.scale(ret, size)
        return ret

class Animation(Image):

    max_w_count = 8

    def __init__(self, size, duration, frames):
        self.duration = duration
        self.frames = frames
        self.frame = 0
        w, h = size
        Image.__init__((w * frames, h))
        pass
