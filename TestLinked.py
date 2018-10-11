from LinkedList import LinkedList
from Node import Node

n1 = Node(130)
n2 = Node(2)
n3 = Node(1)
a = LinkedList()
a.append_head(n1)
print(a.get_head())
a.append_node(n2)
b = a.get_head()
c = b.get_next()
a.append_node(n3)
a.percorror_linked()