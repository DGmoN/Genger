from display import Window, Display
from display import Face
from ui import UIElement, Label, Button, Panel, TextInput, BeatPannel, TileConfigPanel
display = Display((800,600))
window = Window((800,600))

window.dumpContext()

display.run()
