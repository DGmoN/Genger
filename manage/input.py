from pygame import event

import pygame

class Input:
    def __init__(self):
        from visible import Window
        self.actions = {
            pygame.QUIT : [Window.instance.quit]
        }

    def add(self, type, action):
        if(type not in self.actions):
            self.actions[type] = [action]
        else:
            self.actions[type] += [action]

    def handle(self):
        for event in pygame.event.get():
            if event.type in self.actions:
                for func in self.actions[event.type]:
                    func(event)
