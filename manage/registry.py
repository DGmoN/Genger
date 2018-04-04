from __future__ import absolute_import
import uuid

class Registry(object):
    def __init__(self):
        self.items = {}
        pass

    def add_item(self, item, uid):
        self.items[uid] = item
        return id

    def id_in_use(self, uid):
        return (uid in self.items)

    def get_item(self, uid):
        return self.items[uid]
