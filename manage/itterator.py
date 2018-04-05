import sys

class Itterator:
    def __init__(self):
        self.items = []
        pass

    def every(self, action):
        for item in self.items:
            action(item, self)

    def add_item(self, item):
        self.items += [item]

    def del_item(self, item):
        pass
