import uuid

class Registry:
    def __init__(self):
        self.items = {}
        pass

    def add_item(self, item, uid : uuid):
        self.items[uid] = item
        return id

    def contains(self, item):
        return item in self.items.values()

    def id_in_use(self, uid : uuid):
        return (uid in self.items)

    def getItem(self, uid):
        if uid in self.items:
            return self.items[uid]
        return None
