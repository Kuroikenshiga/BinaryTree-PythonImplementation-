import node as nd

class Person(nd.Node):

    def __init__(self, nome):
        self.__nome = nome
        self.idade = 0
        super().__init__(nome)

    def getNome(self):
        return self._Person__nome
    def setNome(self,nome):
        self._Person__nome = nome
