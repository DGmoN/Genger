from display import Window
from display import Face
from ui.UIElement import UIElement
window = Window((800,600))

ff = UIElement()
ff.position = (0,0)
ff.size = (100,100)
window.addItem(ff)
ff.treePos()
window.run()
