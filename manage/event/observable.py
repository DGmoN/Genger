import pygame
from pygame import event
import sys
from manage import Observer
"""
    An Observeable object defines paramaters to flag in the event set
"""

class Observeable:

    EVENT_MOUSE_ENTER = pygame.USEREVENT + 1
    EVENT_MOUSE_LEAVE = pygame.USEREVENT + 2

    EVENT_SENDER = None

    def __init__(self):
        self.observer = None
        self.actions = {}
        self.validations = {}
        self.observables = {}
        pass

    def tree(self):
        tabs = 0
        if self.parent:
            tabs = self.parent.tree()
        for id, act in self.actions.items():
            print(("\t"*tabs), event.event_name(id), "->", act)
        for id, act in self.observables.items():
            for e in act:
                print(("\t"*tabs), event.event_name(id), "->", e)
        return tabs + 1
        pass

    def observe(self, events):
        holder = events
        for i in events:
            if i.type in self.observables:
                for e in self.observables[i.type]:
                    e.observe(holder)
            self.catch(i)
            if(holder):
                holder.pop()


    def addObserveable(self, observable):
        observable.setObserver(self)
        pass

    #returns {event.type: [self.methods]}
    def getHooks(self):
        return list(self.actions.keys()) + list(self.observables.keys())

    def removeObserved(self, observed):
        for e in observed.getHooks():
            if(e in self.observables):
                hooklist = self.observables[e]
                if(observed in hooklist):
                    hooklist.remove(observed)

    def refresh(self, observed):
        self.removeObserved(observed)
        for e in observed.getHooks():
            if(e in self.observables):
                self.observables[e] += [observed]
            else:
                self.observables[e] = [observed]
        count = 0
        if(self.parent):
            count = self.parent.refresh(self)
        print("=="*count, "Refreshed: ",self)
        return count + 1


    def setObserver(self, observer):
        self.observer = observer
        self.observer.refresh(self)

    def addValidator(self,type, val):
        if(type in self.validations):
            self.validations[type] += val
        else:
            self.validations[type] = val

    def addAction(self, type, actions):
        if(type in self.actions):
            self.actions[type] += actions
        else:
            self.actions[type] = actions
        if(self.observer): self.observer.refresh(self)

    #checks if an event is noteable
    def catch(self, event):
        if(event.type in self.actions):
            if event.type in self.validations:
                for val in self.validations[event.type]:
                    if not(val(event)):
                        return
            for action in self.actions[event.type]:
                action(event)
        pass

class MouseObservable(Observeable):

    def __init__(self):
        Observeable.__init__(self)
        self.addAction(pygame.MOUSEMOTION, [self.onMouseMove])
        self.addAction(pygame.MOUSEBUTTONUP, [])
        self.addAction(Observeable.EVENT_MOUSE_ENTER, [self.onMouseEnter])
        self.addAction(Observeable.EVENT_MOUSE_LEAVE, [self.onMouseLeave])
        self.size = (0,0)
        self.position = (0,0)
        self.mouseInside = False
        self.mouseEntered = False
        self.addValidator(pygame.MOUSEMOTION, [self.testMouseMotion])
        self.addValidator(Observeable.EVENT_MOUSE_ENTER, [self.testMouseEntered])
        self.addValidator(Observeable.EVENT_MOUSE_LEAVE, [self.testMouseWasInside])

    def testMouseMotion(self, event):
        self.mouseInside = self.getRect().collidepoint(event.pos)
        if (self.mouseInside and not self.mouseEntered):
            Observeable.EVENT_SENDER = self
            pygame.event.post(pygame.event.Event(Observeable.EVENT_MOUSE_ENTER, event.__dict__))
            self.mouseEntered = True
        elif (not self.mouseInside and self.mouseEntered):
            Observeable.EVENT_SENDER = self
            pygame.event.post(pygame.event.Event(Observeable.EVENT_MOUSE_LEAVE, event.__dict__))
            self.mouseEntered = False
        return self.mouseInside

    def testMouseWasInside(self, event):
        return Observeable.EVENT_SENDER is self

    def testMouseEntered(self, event):
        return self.mouseInside and (Observeable.EVENT_SENDER is self)

    def getPosition(self):
        return self.position

    def getRect(self):
        from pygame import Rect
        return Rect((*self.getPosition(), *self.size))

    def onMouseButtonUp(self, event):
        pass

    def onMouseEnter(self, event):
        pass

    def onMouseLeave(self, event):
        pass

    def onMouseMove(self, event):
        pass

class OWindow(Observeable):
    def __init__(self):
        Observeable.__init__(self)
        self.addAction(pygame.QUIT, [self.onWindowCloseRequest])

    def onWindowCloseRequest(self, event):
        pass

    def onWindowResize(self, event):
        pass

    def onWindowMove(self, event):
        pass
