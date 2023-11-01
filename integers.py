import node

class Integer(node.Node):

    def __init__(self,number):
        self.__number = number
        super().__init__(self.getNumber())

    def getNumber(self):
        return self._Integer__number
    
    def setNumber(self,number):
        self._Integer__number = number
