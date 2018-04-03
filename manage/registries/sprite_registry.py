from manage import Registry
from visible import Sprite
class SpriteRegistry(Registry):
    def registerSprite(self, item, uid, image=None, size=None):
        if not self.id_in_use(uid):
            sprite = item(image)
            self.add_item(sprite, uid)
            print("Sprite registered: ", uid, " >> ", item)
        pass
