from pygame import Rect
class Layout:
    def getMargin(self):
        return Rect((25,5,5,5))

    def placeElements(self, bounds, elements):
        index = 0
        x, y = (0,0)
        mx, my = bounds
        xpad = 0
        margin = self.getMargin()
        y += margin.top
        for e in elements:
            x += margin.left
            w, h = e.getSize()
            if(x + w > mx):
                x = margin.left
                y += h + margin.top
            e.setPosition((x, y))

            x += w
            index +=1

        pass

    def resizeElement(self, container, element, elementIndex):
        pass
