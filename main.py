from visible import Window
from facade import Facade, Face, Block


window = Window((800, 600))
blk = Block()
blk2 = Block()
blk2.setPosition((200,200))
window.addItem(blk)
window.addItem(blk2)
window.run()
