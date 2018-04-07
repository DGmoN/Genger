import pygame
import sys
from manage import Observer
"""
    An Observeable object defines paramaters to flag in the event set
"""

class Observeable:

    EVENT_SENDER = None

    def __init__(self):
        self.observer = None
        self.actions = {}
        self.validations = {}
        pass

    #returns {event.type: [self.methods]}
    def getHooks(self):
        return list(self.actions.keys())

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
        self.addAction(Observer.EVENT_MOUSE_ENTER, [self.onMouseEnter])
        self.addAction(Observer.EVENT_MOUSE_LEAVE, [self.onMouseLeave])
        self.size = (0,0)
        self.position = (0,0)
        self.mouseInside = False
        self.mouseEntered = False
        self.addValidator(pygame.MOUSEMOTION, [self.testMouseMotion])
        self.addValidator(Observer.EVENT_MOUSE_ENTER, [self.testMouseEntered])
        self.addValidator(Observer.EVENT_MOUSE_LEAVE, [self.testMouseWasInside])

    def testMouseMotion(self, event):
        self.mouseInside = self.getRect().collidepoint(event.pos)
        if (self.mouseInside and not self.mouseEntered):
            Observeable.EVENT_SENDER = self
            pygame.event.post(pygame.event.Event(Observer.EVENT_MOUSE_ENTER, event.__dict__))
            self.mouseEntered = True
        elif (not self.mouseInside and self.mouseEntered):
            Observeable.EVENT_SENDER = self
            pygame.event.post(pygame.event.Event(Observer.EVENT_MOUSE_LEAVE, event.__dict__))
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

class SeeingObservable(Observer, Observeable):
    def __init__(self):
        Observer.__init__(self)
        Observeable.__init__(self)

    def catch(self, event):
        Observeable.catch(self, event)
        Observer.observe(self)

class OWindow(SeeingObservable):
    def __init__(self):
        SeeingObservable.__init__(self)
        self.addAction(pygame.QUIT, [self.onWindowCloseRequest])
        self.addObserveable(self)

    def onWindowCloseRequest(self, event):
        pass

    def onWindowResize(self, event):
        pass

    def onWindowMove(self, event):
        pass
