class Node:
    
    def __init__(self,key):
        self.__rigth = None
        self.__left = None
        self.__key = key

    def getRight(self):
        return self._Node__rigth
    def setRight(self,node):
        if not issubclass(type(node),Node) and node != None: 
            raise ValueError('Tipo do nó é invalido')
        self._Node__rigth = node
    
    def getLeft(self):
        return self._Node__left
    def setLeft(self,node):
        if not issubclass(type(node),Node) and node != None: 
            raise ValueError('Tipo do nó é invalido')
        self._Node__left = node

    def getKey(self):
        return self._Node__key
    