import treeBinary as tb
import integers as int
import node as nd
import calendar 
import persons

i1 = int.Integer(4)
i2 = int.Integer(6)
i3 = int.Integer(1)
i4 = int.Integer(0)
i5 = int.Integer(7)
tb = tb.TreeBinary()




# l = [int.Integer(4),int.Integer(8),int.Integer(7),int.Integer(1),int.Integer(3),int.Integer(10),int.Integer(16),int.Integer(0),int.Integer(2),int.Integer(6)]
# l.extend([int.Integer(5), int.Integer(9), int.Integer(11), int.Integer(14), int.Integer(22), int.Integer(33), int.Integer(44), int.Integer(55), int.Integer(66), int.Integer(77),
#           int.Integer(88), int.Integer(99), int.Integer(21), int.Integer(31), int.Integer(41), int.Integer(51), int.Integer(61), int.Integer(71), int.Integer(81), int.Integer(91),
#           int.Integer(101), int.Integer(111), int.Integer(121), int.Integer(131), int.Integer(141), int.Integer(151), int.Integer(161), int.Integer(171), int.Integer(181),
#           int.Integer(191), int.Integer(201), int.Integer(211), int.Integer(221), int.Integer(231), int.Integer(241), int.Integer(251), int.Integer(261), int.Integer(271),
#           int.Integer(281), int.Integer(291), int.Integer(301), int.Integer(311), int.Integer(321), int.Integer(331), int.Integer(341), int.Integer(351), int.Integer(361),
#           int.Integer(371), int.Integer(381)])

nomes = [
    "Alice", "Bob", "Carlos", "Diana", "Eduardo",
    "Fernanda", "Gabriel", "Heloisa", "Igor", "Juliana",
    "Klaus", "Lara", "Mariano", "Nina", "Otávio",
    "Paula", "Quiteria", "Rafael", "Sofia", "Thiago",
    "Ursula"]


l = [persons.Person("Lukas"),persons.Person("João"),persons.Person("Marcelo"),persons.Person("Rogerio")]
for n in nomes:
    tb.insertNode(persons.Person(n))

ex = persons.Person("Rogerio")
print(ex.getNome())

print(ex.getNome())
print("-"*344)
# tb.printTree()
# print('+++++++++++++++++++++++++++++++++++++++++++')
# tb.printTreeBylevel()
# print(type(i))
# print(type(n))
# print(issubclass(type(i),nd.Node))

tb.printTree()
print("-"*30)
tb.callBackFunction(setNames)
tb.printTree()
# tb.printTree()
# print('-'*10)





#Entrada de dados no Python
#numero = input('Insira um número: ')












