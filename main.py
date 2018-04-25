from display import Window, Display
from display import Face
from ui import UIElement, Label, Button, Panel, TextInput, BeatPannel, TileConfigPanel
display = Display((800,600))
window = Window((800,600))
elm = Panel()
elm2 = Panel()
elm3 = Panel()
elm4 = Panel()
elm.setSize((300, 300))
elm2.setSize((100, 100))
elm3.setSize((100, 100))
elm4.setSize((250, 100))
window.addItem(elm)
elm.addItem(elm2)
elm.addItem(elm3)
elm.addItem(elm4)

elm2.dumpContext()
elm3.dumpContext()

display.run()
