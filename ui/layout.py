from pygame import Rect
class Layout:
    def getMargin(self):
        return Rect((5,5,5,5))

    def placeElements(self, bounds, elements):
        index = 0
        lastIndex = 0
        mx, my = bounds
        xpad = 0
        margin = self.getMargin()
        x, y = margin.topleft
        row = self.getRow(elements[index:], mx)
        while row:
            self.distributeX(row, mx, (x,y))
            index += len(row)
            row = self.getRow(elements[index:], mx)
            y += self.maxHeight(row) + margin.top
            row = self.getRow(elements[index:], mx)

    def getRow(self, array, maxX):
        index = 1
        for a in array:
            if(self.sumWidth(array[:index]) > maxX):
                print(self.sumWidth(array[:index]))
                return array[:index - 1]
            index +=1
        return array


    def distributeX(self, elements, max, start):
        x,y = start
        items = len(elements)
        sumw = self.sumWidth(elements)
        inter = (max - sumw - (x * 2))/(items + 1)
        for e in elements:
            w, h = e.getSize()
            x += inter
            e.setPosition((x, y))
            x += w

    def distributeY(self, elements, max):
        pass

    def maxHeight(self, elements):
        max = 0
        for e in elements:
            if(e.getHeight() > max) : max = e.getHeight()
        return max

    def sumWidth(self, elements):
        w = 0
        for e in elements: w += e.getBoudingRect().width
        return w

    def resizeElement(self, container, element, elementIndex):
        pass
