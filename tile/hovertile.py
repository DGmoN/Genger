from facade.facade import Facade
from manage import MouseListner
from visible.sprite import Sprite
from tile import Tile
import pygame
import uuid

class Hovertile(Tile):

    idle_sprite = uuid.uuid1()
    hover_sprite = uuid.uuid1()
    focus_sprite = uuid.uuid1()

    def __init__(self):
        Tile.__init__(self)

    def create_sprite(self, registry):
        registry.registerSprite(Sprite, Hovertile.idle_sprite, "idle_tile.png")
        registry.registerSprite(Sprite, Hovertile.hover_sprite, "hover_tile.png")
        registry.registerSprite(Sprite, Hovertile.focus_sprite, "focus_tile.png")

    def onResize(self, old, new):
        from visible import Window
        Window.instance.get_sprite_registry().get_item(Hovertile.idle_sprite).setSize(self.size)
        Window.instance.get_sprite_registry().get_item(Hovertile.hover_sprite).setSize(self.size)
        Window.instance.get_sprite_registry().get_item(Hovertile.focus_sprite).setSize(self.size)

    def get_sprite(self):
        if(self.focus):
            return Hovertile.focus_sprite
        if(self.inside):
            return Hovertile.hover_sprite
        return Hovertile.idle_sprite

    def onClick(self, event):
        pass
