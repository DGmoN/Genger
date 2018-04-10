class Resources:
    def __init__(self):
        from visible import FontProvider
        from manage import SpriteRegistry, ImageRegistry
        self.sprite_registry = SpriteRegistry()
        self.font_provider = FontProvider()
        self.image_regestry = ImageRegistry()
