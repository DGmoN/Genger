import pygame
from pygame import event
from manage import Itterator
import sys
from manage import Observer
"""
    An Observeable object defines paramaters to flag in the event set
"""

class Observeable(Itterator):

    EVENT_RELEASED = pygame.USEREVENT
    EVENT_MOUSE_ENTER = pygame.USEREVENT + 1
    EVENT_MOUSE_LEAVE = pygame.USEREVENT + 2

    EVENT_SENDER = None

    def __init__(self):
        self.observer = None    #The parent of the observable
        self.actions = {}       #The actions connected to the observeable
        self.validations = {}   #The rules set by each action to test against before excecution
        self.grabbed = {}
        self.observables = []
        self.ungrabbed = []
        pass

    def observeGrabbed(self, events):
        ret = []
        for eve in events:
            if(eve.type in self.grabbed):
                for g in self.grabbed[eve.type]:
                    g.observe(events)
            else:
                ret += [eve]
        return ret

    def observe(self, events):
        que = self.observeGrabbed(events)
        for e in self.ungrabbed:
            e.observe(que)
        for i in que:
            if(i.type in self.actions):
                if(self.testEvent(i)):
                    for e in self.actions[i.type]:
                        e(i)

    def grab(self, type, obs):
        if(type in self.grabbed):
            self.grabbed[type] += [obs]
        else:
            self.grabbed[type] = [obs]
        if(obs in self.ungrabbed):
            self.ungrabbed.remove(obs)

    def release(self, type, obs):
        if(type in self.grabbed):
            if(obs in self.grabbed[type]):
                self.grabbed[type].remove(obs)
            if not(self.grabbed[type]):
                self.grabbed.pop(type, None)

        self.ungrabbed += [obs]

    def testEvent(self, event):
        if(event.type in self.validations):
            for test in self.validations[event.type]:
                if not(test(event)):
                    return False
        return True

    def releaseOnEvent(self, event):
        self.observer.release(event.type, self)

    def addObserveable(self, obs):
        self.observables += [obs]
        self.ungrabbed += [obs]
        obs.observer = self
        print("observer added: ", obs, ":", self)

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
        self.addAction(Observeable.EVENT_RELEASED, [self.onReleased])
        self.addAction(pygame.MOUSEBUTTONUP, [self.onMouseButtonUp])
        self.addValidator(pygame.MOUSEMOTION, [self.isMouseInside])
        self.addValidator(pygame.MOUSEBUTTONUP, [self.isMouseInside])
        self.mouseInside = False
        self.position = (0,0)
        self.size = (0,0)

    def isMouseInside(self, eve):
        wasInside = self.mouseInside
        self.mouseInside = self.getRect().collidepoint(eve.pos)
        if( not wasInside and self.mouseInside):
            self.observer.grab(pygame.MOUSEMOTION, self)
            self.observer.grab(pygame.MOUSEBUTTONUP, self)
            self.onMouseEnter(eve)
        elif(wasInside and not self.mouseInside):
            self.observer.release(pygame.MOUSEMOTION, self)
            self.observer.release(pygame.MOUSEBUTTONUP, self)
            self.onMouseLeave(eve)
        return self.mouseInside
        pass

    def onReleased(self, event):
        #print("Release: ", event.type, self)
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
