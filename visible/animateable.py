
class Animateable:
    def __init__(self):
        self.animations = []

    def addAnimation(self, animation):
        self.animations += [animation]
        animation.animate = self

    def onStep(self):
        pass

    def draw(self):
        pass

    def render(self):
        for e in self.animations: e.step()

class Animation:
    def __init__(self, duration):
        self.duration = duration
        self.time = 0
        self.animate = None
        self.direction = 0
        self.loop = False

    def getCompletion(self):
        return (self.time / self.duration)

    def step(self):
        from visible import Window
        self.time += (Window.last_frame * self.direction)
        if(self.time > self.duration or self.time <= 0):
            if(self.loop):
                self.time -= self.duration
            else:
                if(self.direction > 0):
                    self.time = self.duration
                elif self.direction < 0:
                    self.time = 0
                self.direction = 0

        self.onStep()

    def onStep(self):
        pass
