from facade import Face
from manage import Observeable

class Panel(Face, Observeable):
    def __init__(self):
        Face.__init__(self)
        Observeable.__init__(self)

    def onAdded(self, old, new):
        new.addObserveable(self)
        pass
