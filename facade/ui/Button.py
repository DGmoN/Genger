from facade import Block, Facade
from manage import KeyboardObserveable
from visible import Sequencer
class Label(Facade):
    def __init__(self, text="label"):
        Facade.__init__(self)
        self.text = text
        self.textSurface = None

    def draw(self):
        Facade.draw(self)
        from visible import Window
        self.textSurface  = Window.instance.resources.font_provider.render(text=self.text)
        self.size = self.textSurface.get_size()

    def render(self, surface):
        Facade.render(self, surface)
        if(self.visible):
            surface.blit(self.textSurface, self.position)

    def setText(self, text):
        self.text = text
        from visible import Window
        self.textSurface  = Window.instance.resources.font_provider.render(text=self.text)
        self.setSize(self.textSurface.get_size())

class Button(Block, Label):
    def __init__(self, text="Button", action=None):
        Label.__init__(self, text)
        Block.__init__(self)
        self.action = action

    def setAction(self, action):
        self.action = action

    def onMouseButtonUp(self, event):
        if(event.button == 1 and self.action):
            self.action()

    def draw(self):
        Label.draw(self)
        Block.draw(self)

    def render(self, surface):
        Block.render(self, surface)
        if(self.mouseInside):
            x, y = self.position
            if(self.visible):
                surface.blit(self.textSurface, (x+5, y+5))
        else:
            Label.render(self, surface)

class SequenceCapturePanel(Block, KeyboardObserveable):
    def __init__(self):
        Block.__init__(self)
        KeyboardObserveable.__init__(self)
        self.squence = Sequencer()
        self.addAnimation(self.squence)
        label = Label("Record")
        self.addItem(label)
        self.Awating = Button("<>", self.toggleRecording)
        self.Play = Button(">>", self.run)
        self.Loop = Button(">o<", self.setLoop)
        self.addItem(self.Awating)
        self.addItem(self.Play)
        self.addItem(self.Loop)

    def draw(self):
        Block.draw(self)
        w, h = self.Awating.size
        w1, h1 = self.Play.size
        w2, h2 = self.Loop.size
        x, y = self.size
        self.Awating.setPosition((x-w-w1-w2, 0))
        self.Play.setPosition((x-w1-w2, 0))
        self.Loop.setPosition((x-w2, 0))

    def setLoop(self):
        if self.squence.repeat:
            self.squence.repeat = False
        else:
            self.squence.repeat = True

    def run(self):
        if(self.squence.running):
            self.squence.stop()
        else:
            self.squence.play(1)

    def toggleRecording(self):
        if(self.squence.recording):
            self.squence.stopRecording()
            print(self.squence.keyframes)
            self.Awating.setText("<>")
        else:
            self.squence.record()
            self.Awating.setText("><")
        pass

    def onKeyDown(self, event):
        if(self.squence.recording):
            self.squence.place(event)

class KeyCapturePanel(Block, KeyboardObserveable):

    def __init__(self, onset):
        Block.__init__(self)
        KeyboardObserveable.__init__(self)
        self.Listening = Label("Awaiting input...")
        self.Idle = Label("Change key")
        self.Awaiting = Button("><")
        self.addItem(self.Listening)
        self.addItem(self.Idle)
        self.addItem(self.Awaiting)
        self.Listening.visible = False
        self.setSize((200, 25))
        self.Awaiting.setSize((25,25))
        self.Awaiting.setPosition((175,0))
        self.waiting = False
        self.onSet = onset
        pass

    def setIcon(self, q):
        self.Awaiting.setText("> "+q+" <")
        x, y = self.Awaiting.size
        w, h = self.size
        self.Awaiting.setPosition((w-x, 0))

    def onKeyUp(self, event):
        if(self.waiting):
            self.onSet(event.key)
            self.waiting = False
            self.Listening.visible = False
            self.Idle.visible = True

    def onMouseButtonUp(self, event):
        if(event.button == 1 and not self.waiting):
            self.waiting = True
            self.Listening.visible = True
            self.Idle.visible = False
