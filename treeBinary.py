import node as nd
class TreeBinary:

    def __init__(self):
        self.__root = None
        self.__size = 0

    def getSize(self):
        return self._TreeBinary__size
    def treeSize(self):
        return self.__size

    def setRoot(self,node):
        if not issubclass(type(node),nd.Node): 
            raise ValueError('Tipo do nó é invalido')
        self._TreeBinary__root = node

    def getRoot(self):
        return self._TreeBinary__root
    
    def insertNode(self,node):
        if not issubclass(type(node),nd.Node): 
            raise ValueError('Tipo do nó é invalido')
        if self.getRoot() == None:
            self.setRoot(node)
            self.__size = self.__size+1
            return True
        return self._TreeBinary__insertNode(self.getRoot(),node)

    def __insertNode(self,root,node):
        if root.getKey() < node.getKey():
            if root.getRight() == None:
                root.setRight(node)
                self.__size = self.__size+1
                return True
            return self._TreeBinary__insertNode(root.getRight(),node)
        if root.getKey() > node.getKey():
            if root.getLeft() == None:
                root.setLeft(node)
                self.__size = self.__size+1
                return True
            return self._TreeBinary__insertNode(root.getLeft(),node)
        return False
    
    def printTree(self):
        self._TreeBinary__printTree(self.getRoot()) if self.getRoot() != None else print('Empty')
    def __printTree(self,root):
        if root.getLeft() != None: self._TreeBinary__printTree(root.getLeft())
        print(root.getKey())
        if root.getRight() != None: self._TreeBinary__printTree(root.getRight())
    
    def depthSearch(self,key):
        return self._TreeBinary__depthSearch(self.getRoot(),key)
    def __depthSearch(self,node,key):
        if(node == None):return None
        
        if(node.getKey() == key):
            return node
        if(key > node.getKey()):
            return self._TreeBinary__depthSearch(node.getRight(),key)
        if(key < node.getKey()):
            return self._TreeBinary__depthSearch(node.getLeft(),key)
        
    
    def breadthSearch(self,key):
        array = [self.getRoot()]
        return self._TreeBinary__breadthSearch(0,key,array)
    
    def __breadthSearch(self,index,key,array):
        try:    
            if(array[index].getKey() == key):
                return array[index]
            if(array[index].getLeft()!=None):array.append(array[index].getLeft())
            if(array[index].getRight()!=None):array.append(array[index].getRight())
        except:
            return None
        return self._TreeBinary__breadthSearch(index+1,key,array)

    def removeNode(self,key):
        return self._TreeBinary__removeNode(self.getRoot(),key)
    def __removeNode(self,node,key):
        if(node.getKey() == key):
            rigth = node.getRight()
            left = node.getLeft()
            newNode = self._TreeBinary__smallestNode(node.getRight()) if node.getRight() != None else self.__TreeBinary__biggestNode(node.getLeft())
            self.removeNode(newNode.getKey())
            newNode.setLeft(left)
            newNode.setRight(rigth)
            self.setRoot(newNode)
            return True
        
        if(node.getKey() > key):
            if(node.getLeft().getKey() == key):
                if(node.getLeft().getLeft() == None and node.getLeft().getRight() == None):
                    node.setLeft(None)
                    return True
                
                newNode = self._TreeBinary__smallestNode(node.getLeft().getRight()) if node.getLeft().getRight() != None else self._TreeBinary__biggestNode(node.getLeft().getLeft())
                self.removeNode(newNode.getKey())
                right = node.getLeft().getRight()
                left = node.getLeft().getLeft()
                newNode.setLeft(left)
                newNode.setRight(right)
                node.setLeft(newNode)
                return True
            return self._TreeBinary__removeNode(node.getLeft(),key)
        if(node.getKey() < key):
            if(node.getRight().getKey() == key):
                if(node.getRight().getLeft() == None and node.getRight().getRight() == None):
                    node.setRight(None)
                    return True

                newNode = self._TreeBinary__smallestNode(node.getRight().getRight()) if node.getRight().getRight() != None else self._TreeBinary__biggestNode(node.getRight().getLeft())
                self.removeNode(newNode.getKey())
                right = node.getRight().getRight()
                left = node.getRight().getLeft()
                newNode.setLeft(left)
                newNode.setRight(right)
                node.setRight(newNode)
                return True
            return self._TreeBinary__removeNode(node.getRight(),key)
        return False

    def smallestNode(self):
        return self._TreeBinary__smallestNode(self.getRoot())
    
    def __smallestNode(self,root):
        return self._TreeBinary__smallestNode(root.getLeft()) if root.getLeft() != None else root
    def biggestNode(self):
        return self._TreeBinary__smallestNode(self.getRoot())
    
    def __biggestNode(self,root):
        return self._TreeBinary__smallestNode(root.getRight()) if root.getRight() != None else root
    
    def callBackFunction(self,callBack):
        self._TreeBinary__callBackFunction(self.getRoot(),callBack)
    def __callBackFunction(self,root,callBack):
        if(root.getLeft() != None): self._TreeBinary__callBackFunction(root.getLeft(),callBack)
        callBack(root)
        if(root.getRight() != None): self._TreeBinary__callBackFunction(root.getRight(),callBack)

    