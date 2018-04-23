from display.Placement import Image
from display.Effect import PlainColor
import pygame

pygame.init()
class Display(Image):
    def create_image(self):
        self.surface = pygame.display.set_mode(self.contextData.size)

panel = Image((250,250))
background = Image((100,100))
foreground = Image((50, 50))
background.addPainter("baseColor",PlainColor((100,100,100)))
foreground.addPainter("foregroundColor",PlainColor((250,100,100)))
panel.linkImage(background)
panel.linkImage(foreground)
display = Display((300,300))
display.linkImage(panel)
display.render()
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        if e.type == pygame.MOUSEMOTION:
            foreground.getContext().pos = e.pos
    if not running: break
    pygame.display.flip()
