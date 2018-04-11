from visible import Window
from facade import Panel
from app import BeatTile

size = (100, 100)

window = Window((800, 600))
beatPanel = Panel()
beatPanel.setSize((600,600))
for y in range(6):
    for x in range(6):
        tile = BeatTile()
        tile.setSize(size)
        w, h = size
        tile.setPosition(((w*x),(h*y)))
        beatPanel.addItem(tile)
window.addItem(beatPanel)
window.run()
