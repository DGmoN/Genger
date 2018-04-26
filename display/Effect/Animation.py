

class Animation:
    def __init__(self, context, attr, duration):
        self.context = context
        self.attr = attr
        self.time = 0
        self.duration = duration
        self.valueHolder = None
        self.direction = 0
        self.destVal = None
        self.dif = None
        from display.render import Display
        Display.ANIMATION_CONTEXT.addContextListner("lastTick", self.onTick)

    def play(self, destVal):
        if(self.direction == 0):
            self.valueHolder = self.context.__dict__[self.attr]
            self.destVal = destVal
            self.dif =  self.destVal - self.valueHolder
            self.direction = 1
            print("playing")
        pass

    def reverse(self):
        self.direction = -1

    def onTick(self, last, next):
        self.time += next * self.direction
        self.step()

    def step(self):
        if(self.time >= self.duration):
            self.time = self.duration
            self.direction = 0
            self.context.__dict__[self.attr] = self.destVal
            return
        if(self.time < 0):
            self.time = 0
            self.direction = 0
            self.context.__dict__[self.attr] = self.valueHolder
            return
        if(self.direction != 0):
            val = int(self.valueHolder + (self.dif * (self.time/self.duration)))
            exec("self.context."+self.attr+" = val")
