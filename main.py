from visible import Window
from facade import Panel
from app import BeatTile
from manage import Observeable
import pygame
from facade import UI
from visible import Resise

class BeatControllPanel(Panel):

    def __init__(self):
        Panel.__init__(self)
        self.ss = UI.SequenceCapturePanel()
        self.ss.setSize((200,100))
        self.ss.setPosition((0, 0))
        self.addItem(self.ss)
        self.setSize((200, 600))
        self.setPosition((600,0))

class TileConfigPanel(Panel):
    LBlockPos = UI.Label("BlockPosition")
    LBlocKey = UI.KeyCapturePanel(None)
    BtnClosePanel = UI.Button("Close")
    def __init__(self):
        Panel.__init__(self)
        self.motion = Resise(500)
        self.motion.addKeyFrame(0, (0,0))
        self.motion.addKeyFrame(0.5, (100,150))
        self.motion.addKeyFrame(1, (200,300))
        self.size = (0,0)
        self.display = False
        self.addItem(TileConfigPanel.LBlockPos)
        self.addItem(TileConfigPanel.LBlocKey)
        self.addItem(TileConfigPanel.BtnClosePanel)
        TileConfigPanel.BtnClosePanel.setAction(self.close)
        TileConfigPanel.BtnClosePanel.setPosition((0,230))
        self.addAnimation(self.motion)
        w, h = TileConfigPanel.LBlockPos.size
        TileConfigPanel.LBlocKey.setPosition((0, h))
        self.tile = None
        TileConfigPanel.LBlocKey.onSet = self.setTileKey

    def close(self):
        self.releaseEvent()
        self.motion.play(-1)

    def setTileKey(self, ke):
        self.tile.key = ke
        from pygame import key
        TileConfigPanel.LBlocKey.setIcon(key.name(self.tile.key))

    def inspectTile(self, tile):
        self.grabEvent()
        self.tile = tile
        MainGamePanel.beatPanel.releaseEvent()
        x, y = tile.position
        w,h = tile.size
        nx = x + (w/2)
        ny = y + (h/2)
        if(ny + 300> 600):
            ny -= 300
        if nx + 200 > 600:
            nx -= 200
        self.setPosition((nx, ny))
        TileConfigPanel.LBlockPos.setText(str((x,y)))
        w2,h2 = TileConfigPanel.LBlockPos.size
        TileConfigPanel.LBlockPos.setPosition(( 100-(w2/2), 0 ))
        self.motion.play(1)
        from pygame import key
        TileConfigPanel.LBlocKey.setIcon(key.name(tile.key))

class MainGamePanel(Panel):
    beatPanel = Panel()
    beatControlls = UI.SequenceCapturePanel()
    tileConfig = TileConfigPanel()

    def __init__(self):
        Panel.__init__(self)
        self.setSize((800, 600))
        MainGamePanel.beatPanel.setSize((600, 600))
        size = (100, 100)
        self.setPosition((0,0))
        count = 0
        for y in range(6):
            for x in range(6):
                tile = BeatTile()
                tile.setSize(size)
                w, h = size
                tile.setPosition(((w*x),(h*y)))
                tile.key = pygame.K_a + count
                count += 1
                MainGamePanel.beatPanel.addItem(tile)
        MainGamePanel.beatControlls.setPosition((600,0))
        MainGamePanel.beatControlls.setSize((200, 400))
        self.addItem(MainGamePanel.beatPanel)
        self.addItem(MainGamePanel.beatControlls)
        self.addItem(MainGamePanel.tileConfig)

window = Window((800, 600))
window.addItem(MainGamePanel())
window.run()
