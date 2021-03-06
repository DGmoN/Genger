import pygame
from visible import ImageSequence
class Animateable:
    def __init__(self):
        self.animations = []

    def addAnimation(self, animation):
        self.animations += [animation]
        animation.animate = self

    def onStep(self, animation):
        pass

    def onComplete(self, animation):
        pass

    def draw(self):
        pass

    def paintAnimation(self, surface):
        for e in self.animations:
            e.paint(surface)

    def run(self):
        for e in self.animations: e.step()

class Animation:
    def __init__(self, duration):
        self.duration = duration
        self.keyframes = {}
        self.time = 0
        self.animate = None
        self.direction = 0
        self.loop = False
        self.repeat = False
        self.circular = False
        self.running = False

    def addKeyFrame(self, time, data):
        self.keyframes[time] = data

    def getKeyframes(self):
        current_pos = self.getCompletion()
        keys = list(self.keyframes.keys())
        if(len(keys) == 2):
            return (self.keyframes[keys[0]], self.keyframes[keys[1]], current_pos)
        upList = [ i for i in keys if i >= current_pos]
        lowList = [ i for i in keys if i <= current_pos]
        if(upList):
            upper = min(upList, key=lambda x:abs(x-current_pos))
        else:
            upper = 0
        if(lowList):
            lower = min(lowList, key=lambda x:abs(x-current_pos))
        else:
            lower = 0
        base = upper - lower
        if(base == 0):
            return (self.keyframes[lower], self.keyframes[upper], 1)
        if(lower == 0):
            return (self.keyframes[upper], self.keyframes[upper], (current_pos - lower) / base)
        if(upper == 0):
            return (self.keyframes[lower], self.keyframes[lower], 1)
        return (self.keyframes[lower], self.keyframes[upper], (current_pos - lower) / base)

    def play(self, direction):
        self.direction = direction
        self.running = True

    def stop(self, compleate=False):
        if(not self.repeat):
            self.time = 0
        self.running = False

    def onComplete(self):
        pass

    def getCompletion(self):
        return (self.time / self.duration)

    def step(self):
        if(not self.running):
            return
        self.onStep()
        self.animate.onStep(self)

        from display import Window
        self.time += (Window.last_frame * self.direction)
        if(self.time > self.duration): self.time = self.duration
        elif(self.time < 0): self.time = 0
        if(self.time >= self.duration or self.time <= 0):
            if(self.circular):
                if(self.direction > 0):
                    self.direction = -1
                else:
                    self.direction = 0
                    self.running = False
                    self.onComplete()
                    self.animate.onComplete(self)
            elif(self.repeat):
                self.time = 0
            elif(self.loop):
                self.direction *= -1
            else:
                self.running = False
                self.onComplete()
                self.animate.onComplete(self)

        if(self.direction == 0):
            self.running = False

    def onStep(self):
        pass

    def getImage(self):
        pass

    def paint(self, surface):
        pass

class ImageChange(Animation):
    def __init__(self, duraion):
        Animation.__init__(self, duraion)
        self.squares = 0
        self.currentImage = pygame.Surface((0,0))
        self.image = None

    def setImage(self, image: ImageSequence):
        self.image = image
        frames = len(self.keyframes)
        import math
        image.squares = int(math.ceil(math.sqrt(frames)))
        image.frames = frames

    def onStep(self):
        c1, c2, dd = self.getKeyframes()
        self.currentImage = self.image.getSubsurface(c1)

    def onComplete(self):
        c1, c2, dd = self.getKeyframes()
        self.currentImage = self.image.getSubsurface(c2)

    def getImage(self):
        return self.currentImage

    def paint(self, surface):
        surface.blit(self.getImage(), (0,0))

class ColourChange(Animation):
    def __init__(self, duration):
        Animation.__init__(self, duration)
        self.currentCollor = (0,0,0)

    def onStep(self):
        c1, c2, dd = self.getKeyframes()
        r1, g1, b1 = c1
        r2, g2, b2 = c2
        rd, gd, bd = (r2 - r1), (g2 - g1), (b2 - b1)
        self.currentCollor = ((int(rd * dd) + r1), (int(gd * dd) + g1), (int(bd * dd) + b1))

        pass

    def paint(self, surf):
        if(self.currentCollor):
            surf.fill(self.currentCollor, surf.get_rect().inflate(-1,-1) ,special_flags=pygame.BLEND_MULT)

    def onComplete(self):
        a, b, c = self.getKeyframes()
        if(c > 0.5):
            self.currentCollor = b
        else:
            self.currentCollor = a

class Motion(Animation):
    def __init__(self, duration):
        Animation.__init__(self, duration)
        self.location = (0,0)

    def onStep(self):
        c1, c2, dd = self.getKeyframes()
        x1, y1 = c1
        x2, y2 = c2
        dx, dy = (x2 - x1), (y2 - y1)
        self.location = (((dd*dx) + x1, (dd * dy)+y1))
        self.animate.setPosition(self.location)
        print(self.getKeyframes())

    def onComplete(self):
        a, b, c = self.getKeyframes()
        self.location = b

class Resise(Animation):
    def __init__(self, duration):
        Animation.__init__(self, duration)
        self.size = (0,0)

    def onStep(self):
        c1, c2, dd = self.getKeyframes()
        x1, y1 = c1
        x2, y2 = c2
        dx, dy = (x2 - x1), (y2 - y1)
        self.size = (int((dd*dx) + x1), int((dd * dy)+y1))
        self.animate.setSize(self.size)

    def onComplete(self):
        c1, c2, dd = self.getKeyframes()
        dd = self.getCompletion()
        if dd > 0.5:
            self.animate.setSize(c2)
        else:
            self.animate.setSize(c1)
        pass

class Sequencer(Animation):
    def __init__(self):
        Animation.__init__(self, 0)
        self.Buffer = {}
        self.recording = False

    def record(self):
        self.recording = True

    def stopRecording(self):
        self.recording = False
        for time, data in self.Buffer.items():
            frame = time/self.time
            self.addKeyFrame(frame, data)
        self.Buffer = {}
        self.duration = self.time
        print("Sequence saved:")
        print("Duration:",self.duration)
        print("Frames:", len(self.keyframes))
        self.time = 0

    def onStep(self):
        c1, c2, dd = self.getKeyframes()
        from pygame import event
        if(dd > 0.5):
            event.post(c2)
        else:
            event.post(c1)
        pass

    def place(self, data):
        self.Buffer[self.time] = data

    def step(self):
        if not self.recording:
            Animation.step(self)
        else:
            from visible import Window
            self.time += (Window.last_frame)
