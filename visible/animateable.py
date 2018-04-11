
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

    def render(self, surf):
        for e in self.animations: e.step()
        for e in self.animations: e.applyRender(surf)

class Animation:
    def __init__(self, duration):
        self.duration = duration
        self.time = 0
        self.animate = None
        self.direction = 0
        self.loop = False

    def onComplete(self):
        self.time = 0
        pass

    def getCompletion(self):
        return (self.time / self.duration)

    def step(self):
        from visible import Window
        self.time += (Window.last_frame * self.direction)
        if(self.time > self.duration or self.time <= 0):
            self.direction = 0
            self.onComplete()

        self.onStep()

    def onStep(self):
        pass

    def applyRender(self, surf):
        pass
