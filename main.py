from display import Window, Display
from display import Face
from ui import UIElement, Label, Button, Panel, TextInput, BeatPannel, TileConfigPanel
display = Display((800,600))
window = Window((800,600))
elm = UIElement()
elm.setSize((100,100))
elm.setPosition((100,100))
window.addItem(elm)
window.dumpContext()

display.run()
