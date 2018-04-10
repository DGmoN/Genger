from visible import Window
from facade import Facade, Face, Block


window = Window((800, 600))
blk = Block()
blk.setSize((300,300))
blk2 = Block()
blk2.setPosition((50,50))
blk.addItem(blk2)
window.addItem(blk)
#blk2.tree();
window.run()
