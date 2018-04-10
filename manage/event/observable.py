import pygame
from pygame import event
from manage import Itterator
import sys
from manage import Observer
"""
    An Observeable object defines paramaters to flag in the event set
"""

class Observeable(Itterator):

    EVENT_MOUSE_ENTER = pygame.USEREVENT + 1
    EVENT_MOUSE_LEAVE = pygame.USEREVENT + 2

    EVENT_SENDER = None

    def __init__(self):
        self.observer = None    #The parent of the observable
        self.actions = {}       #The actions connected to the observeable
        self.validations = {}   #The rules set by each action to test against before excecution
        self.observables = []
        pass

    def observe(self, events):
        for e in self.observables:
            e.observe(events)
        for i in events:
            if(i.type in self.actions):
                if(self.testEvent(i)):
                    for e in self.actions[i.type]:
                        e(events)

    def testEvent(self, event):
        if(event.type in self.validations):
            for test in self.validations[event.type]:
                if not(test(event)):
                    return False
        return True

    def addObserveable(self, obs):
        self.observables += [obs]
        print(self.observables)

    def addAction(self, type, action):
        if(type in self.actions):
            self.actions[type] += action
        else:
            self.actions[type] = action

    def addValidator(self, type, action):
        if(type in self.validations):
            self.validations[type] += action
        else:
            self.validations[type] = action

    def list_events(self):
        for ev, actions in self.actions.items():
            print(event.event_name(ev), actions)


class MouseObservable(Observeable):

    def __init__(self):
        Observeable.__init__(self)
        self.addAction(pygame.MOUSEMOTION, [self.onMouseMove])
        self.addAction(Observeable.EVENT_MOUSE_ENTER, [self.onMouseEnter])
        self.addAction(Observeable.EVENT_MOUSE_LEAVE, [self.onMouseLeave])
        self.addValidator(pygame.MOUSEMOTION, [self.isMouseInside])
        self.addValidator(Observeable.EVENT_MOUSE_ENTER, [self.isMouseInside])
        self.mouseInside = False
        self.position = (0,0)
        self.size = (0,0)

    def isMouseInside(self, eve):
        wasInside = self.mouseInside
        self.mouseInside = self.getRect().collidepoint(eve.pos)
        if( not wasInside and self.mouseInside):
            event.post(event.Event(Observeable.EVENT_MOUSE_ENTER, eve.__dict__))
        elif(wasInside and not self.mouseInside):
            event.post(event.Event(Observeable.EVENT_MOUSE_LEAVE, eve.__dict__))

        return self.mouseInside
        pass

    def getAbsolutePosition(self):
        return self.position

    def getRect(self):
        from pygame import Rect
        return Rect((*self.getAbsolutePosition(), *self.size))

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
