from display import Window
from display import Face
from ui import UIElement, Label, Button, Panel, TextInput, BeatTile
window = Window((800,600))

pan = Panel()
pan.setSize((200,200))


ff = BeatTile()
ff.setPosition((0,0))
ff.setSize((100,100))
pan.addItem(ff)
window.addItem(pan)
ff.treePos()
window.run()
