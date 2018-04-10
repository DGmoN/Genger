from manage import Registry
import uuid
class ImageRegistry(Registry):
    def registerImage(self, item, uid=None):
        if not uid:
            uid = uuid.uuid1()
        self.add_item(item, uid)
        print("Image updated: ", uid, " >> ", item)
        return uid
