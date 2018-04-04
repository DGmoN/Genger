from __future__ import absolute_import
from pygame.font import Font

class FontProvider(object):

    Fonts = None

    def __init__(self):
        FontProvider.Fonts = {
            u"default" : Font(u"C:/Windows/Fonts/ariblk.ttf", 16)
        }

    def render(self,text, font=u"default", color=(255,255,255)):
        return FontProvider.Fonts[font].render(text, True, color)
