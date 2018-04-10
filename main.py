from visible import Window
from facade import Facade, Face, Block


window = Window((800, 600))
blk = Block()
blk.setSize((300,300))
qqq = Block()
qqq.setPosition((20,20))
blk.addItem(qqq)
blk2 = Block()
blk2.setPosition((300,50))
blk2.setSize((300,300))
"""blk3 = Block()
blk3.setPosition((350,50))
blk.addItem(blk2)
#window.addItem(blk3)"""
window.addItem(blk)
window.addItem(blk2)
window.list_events()
window.run()
