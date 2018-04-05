from pygame.font import Font

class FontProvider:

    Fonts = None

    def __init__(self):
        FontProvider.Fonts = {
            "default" : Font("C:/Windows/Fonts/ariblk.ttf", 16)
        }

    def render(self,text, font="default", color=(255,255,255)):
        return FontProvider.Fonts[font].render(text, True, color)
