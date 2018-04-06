from pygame import event

import pygame

class Input:

    EventGroups = {
        "mouse" : [ pygame.MOUSEMOTION,
                    pygame.MOUSEBUTTONUP,
                    pygame.MOUSEBUTTONDOWN]
    }

    def __init__(self):
        self.actions = {}

    def addAction(self, type, action):
        if(type not in self.actions):
            self.actions[type] = [action]
        else:
            self.actions[type] += [action]

    def addActionGroup(self, group, action):
        for e in group:
            self.addAction(e, action)

    def testEvents(self):
        self.die = False
        for event in pygame.event.get():
            if event.type in self.actions:
                for func in self.actions[event.type]:
                    func(event)
