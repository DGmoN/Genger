from display import Window, Display
from display import Face
from ui import UIElement, Label, Button, Panel, TextInput, BeatPannel, TileConfigPanel, BeatTile
display = Display((800,600))
window = Window((800,600))
TilePanel = Panel()
GridConfigs = Panel()
TileInfo = Panel()
Loops = Panel()
AudioOut = Panel()
TilePanel.setSize((600, 450))
for e in range(12):
    TilePanel.addItem(BeatTile())
GridConfigs.setSize((200, 450))
GridConfigs.setPosition((600, 0))

TileInfo.setSize((400, 150))
TileInfo.setPosition((400,450))

Loops.setSize((300, 150))
Loops.setPosition((100, 450))

AudioOut.setSize((100, 150))
AudioOut.setPosition((0, 450))

window.addItem(TilePanel)
window.addItem(GridConfigs)
window.addItem(TileInfo)
window.addItem(Loops)
window.addItem(AudioOut)

display.run()
