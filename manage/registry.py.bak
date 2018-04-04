import uuid

class Registry:
    def __init__(self):
        self.items = {}
        pass

    def add_item(self, item, uid : uuid):
        self.items[uid] = item
        return id

    def id_in_use(self, uid : uuid):
        return (uid in self.items)

    def get_item(self, uid):
        return self.items[uid]
