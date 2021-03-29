class Protected:
    def __init__(self):
        self._protected = 0  # This is my protected attribute. It can be accessed and modified
        self.__privateVar = 0  # This is my private attribute. It can still be modified or read, but..
        # we include methods to do so, this prevents the variable from changing on accident

    def getPrivate(self):   # Functions to access and modify my private var
        print(self.__privateVar)

    def setPrivate(self, setValue):
        self.__privateVar = setValue


obj = Protected()
obj._protected = 34
print(obj._protected)

obj.getPrivate()
obj.setPrivate(23)
myPrivateVar = obj.getPrivate()
print(myPrivateVar)