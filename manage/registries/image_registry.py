from manage import Registry
import uuid
class ImageRegistry(Registry):
    def registerImage(self, item, uid=None):
        if not uid:
            uid = uuid.uuid1()
        if self.id_in_use(uid):
            item.uuid = uid
            return uid
        self.add_item(item, uid)
        item.uuid = uid
        print("Image updated: ", uid, " >> ", item)
        return uid

    def getItem(self, uuid):
        item = Registry.getItem(self, uuid)
        if(item): item.uuid = uuid
        return item
