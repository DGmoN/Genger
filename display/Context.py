class Context:
    def __init__(self):
        self.contextListners = {} #A variable name and functions to call on thier changes
        self.hasChanged = False

    def addContextListner(self, name, function):
        if(name in self.__dict__):
            if(name in self.contextListners):
                self.contextListners[name] += [function]
            else:
                self.contextListners[name] = [function]

    def handleContextChange(self, name, old, new):
        if("contextListners" in self.__dict__):
            if(name in self.contextListners):
                self.hasChanged = True
                print("Context changed: ", name, new)
                for f in self.contextListners[name]:
                    if(f):
                        f(old, new)

    def clearChange(self):
        self.hasChanged = False

    def dumpContext(self):
        for e in self.contextListners.keys():
            print(e, " = ", self.__dict__[e])

    def __setattr__(self, name, value):
        try:

            if(name in self.__dict__):
                old = self.__dict__[name]
                self.__dict__[name] = value
                self.handleContextChange(name, old, value)
            else:
                self.__dict__[name] = value
        except AttributeError as e:
            print("Context has no attr: ",name)
            raise e
