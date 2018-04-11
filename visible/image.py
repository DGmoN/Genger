from pygame import Surface

class Image:
    def __init__(self, size):
        self.size = size
        self.sprites = []
        self.surface = Surface(size).convert_alpha()
        self.drawn = False

    def addSprite(self, spriteClass):
        if(spriteClass in self.sprites):
            return
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

class ImageSequence(Image):
    def __init__(self, size):
        Image.__init__(self, size)
        self.squares = 0
        self.frames = 0

    def getSubsurface(self, frame):
        row = int(frame / self.squares)
        col = int(frame % self.squares)
        w, h = self.size
        return self.surface.subsurface((w*row, h*col, w, h))

    def draw(self):
        from pygame import Surface
        import pygame
        from visible import Window
        w, h = self.size
        self.surface = Surface((w*self.squares, h*self.squares)).convert_alpha()
        self.surface.fill(Window.transparent)
        for i in range(self.frames):
            for e in self.sprites:
                sprite = Window.get_sprite_registry().get_item(e)
                sprite.mutation = i/self.frames
                sprite.render(self.getSubsurface(i))
        pygame.image.save(self.surface, "hell.png")
        print("drew: ", self)
