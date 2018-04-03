class Listner:
    def __init__(self, type):
        from visible import Window
        Window.instance.input.add(type, self.handle)

    def handle(self, event):
        pass

class MouseListner(Listner):
    def handle(self, event):
        pass
