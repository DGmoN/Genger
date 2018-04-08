from pygame import event

class Observer:



    def __init__(self):
        #the hooks are the only events the observer will be observing
        self.observables = {}
        pass

    def observe(self):
        events = event.get()
        for i in events:
            if i.type in self.observables:
                for e in self.observables[i.type]:
                    e.catch(i)

    def addObserveable(self, observable):
        for i in observable.getHooks():
            if i in self.observables:
                if not observable in self.observables[i]:
                    self.observables[i] += [observable]
            else:
                self.observables[i] = [observable]
            print("Hooked: ", i, " to ", observable)
        observable.parent = self

        pass
