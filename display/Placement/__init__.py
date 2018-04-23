class ImageContext:
    def __init__(self):
        self.changed = False
        self.contextData = {}

    def __getattr__(self, name):
        if(name in self.__dict__):
            return self.__dict__[name]

        try:
            if(name in self.contextData):
                return self.contextData[name]
        except AttributeError as e:
            print("Contect has no attr: ",name)
            raise e

    def hasChanged(self):
        if(self.changed):
            self.changed = False
            return True
        return False

    def __setattr__(self, name, value):
        try:
            if('contextData' in self.__dict__):
                self.__dict__['contextData'][name] = value
                self.changed = True
            else:
                self.__dict__[name] = value
        except AttributeError as e:
            print("Contect has no attr: ",name)
            raise e


from display.Placement.ImageClass import Image
