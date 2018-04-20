import pygame
from pygame import event
from manage import Itterator
import sys
"""
    An Observeable object defines paramaters to flag in the event set
"""

class Observeable(Itterator):

    EVENT_RELEASED = pygame.USEREVENT
    EVENT_TEST = pygame.USEREVENT + 1
    GRAB = None#pygame.MOUSEBUTTONUP

    def __init__(self):
        if(hasattr(self, "created")):
            return
        self.observer = None    #The parent of the observable
        self.actions = {}       #The actions connected to the observeable
        self.validations = {}   #The rules set by each action to test against before excecution
        self.grabbed = []
        self.observables = []
        self.ungrabbed = []
        self.created = True
        self.addAction(Observeable.EVENT_TEST, [self.onTestRecieved])
        pass

    def onTestRecieved(self, event):
        print(event.depth * "-", self)
        event.depth+=1

    def getActionKeys(self):
        return list(self.actions.keys())

    def observe(self, events):
        if not (events):
            return []
        exclusion_ids = []
        clean = events.copy()
        for e in self.grabbed:
            holder = e.observe(events) # returns the observers exclusion id list
            for i in holder:
                if(i not in exclusion_ids):
                    exclusion_ids += [i]
                if(i in clean):
                    clean.remove(i)
        for e in self.ungrabbed:
            e.observe(clean)
        for i in clean:
            if(i not in exclusion_ids):
                if(i.type in self.actions):
                    if(self.testEvent(i)):
                        for e in self.actions[i.type]:
                            e(i)
                        if i.type == Observeable.GRAB:
                            print("Event debug: ",self)
        return exclusion_ids

    def grabEvent(self):
        if(self.observer):
            self.observer.grab(self)
            print("Grabbed", self)

    def isGrabbed(self, type, obj):

        return type in self.grabbed.keys() and obj in self.grabbed[type]

    def releaseEvent(self):
        if(self.observer):
            self.observer.release(self, self)
            print("Released", self)

    def grab(self, obs):
        if(obs in self.grabbed):
            return
        if(obs in self.ungrabbed):
            self.ungrabbed.remove(obs)
            self.grabbed += [obs]

    def release(self, type, obs):
        if(obs in self.ungrabbed):
            return
        if(obs in self.grabbed):
            self.grabbed.remove(obs)
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

    def tree(self):
        depth = 0
        if(self.parent):
            depth = self.parent.tree()
        print(">>"*depth, self)
        print("+"*depth, "Grabbed:")
        for e in self.grabbed:
            print(("-"*depth)+ ">",e)
        print("+"*depth, "Observables:")
        for e in self.observables:
            print(("-"*depth)+ ">",e)
        print("+"*depth, "Events:")
        for e in self.actions:
            print(("-"*depth)+ ">",event.event_name( e))
        return depth + 1


class MouseObservable(Observeable):

    def __init__(self):
        Observeable.__init__(self)
        self.addAction(pygame.MOUSEMOTION, [self.onMouseMove])
        self.addAction(Observeable.EVENT_RELEASED, [self.onReleased])
        self.addAction(pygame.MOUSEBUTTONUP, [self.onMouseButtonUp])
        self.addAction(pygame.MOUSEBUTTONDOWN, [self.onMouseButtonDown])
        self.addValidator(pygame.MOUSEMOTION, [self.isMouseInside])
        self.addValidator(pygame.MOUSEBUTTONUP, [self.isMouseInside])
        self.addValidator(pygame.MOUSEBUTTONDOWN, [self.isMouseInside])
        self.mouseInside = False
        self.position = (0,0)
        self.size = (0,0)

    def isMouseInside(self, eve):
        wasInside = self.mouseInside
        self.mouseInside = self.getAbsoluteRect().collidepoint(eve.pos)
        if( not wasInside and self.mouseInside):
            self.onMouseEnter(eve)
        elif(wasInside and not self.mouseInside):
            self.onMouseLeave(eve)
        return self.mouseInside
        pass

    def onReleased(self, event):
        #print("Release: ", event.type, self)
        pass

    def getAbsolutePosition(self):
        return self.position

    def getAbsoluteRect(self):
        from pygame import Rect
        return Rect((*self.getAbsolutePosition(), *self.size))

    def onMouseButtonUp(self, event):
        pass

    def onMouseButtonDown(self, event):
        pass

    def onMouseEnter(self, event):
        pass

    def onMouseLeave(self, event):
        pass

    def onMouseMove(self, event):
        pass

class KeyboardObserveable(Observeable):
    def __init__(self):
        Observeable.__init__(self)
        self.addAction(pygame.KEYUP, [self.onKeyUp])
        self.addAction(pygame.KEYDOWN, [self.onKeyDown])

    def onKeyUp(self, event):
        pass

    def onKeyDown(self, event):
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
