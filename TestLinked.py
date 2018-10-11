from structure import LinkedList as lk
from structure import SimpleNode as no


n1 = no.SimpleNode(130)
n2 = no.SimpleNode(2)
n3 = no.SimpleNode(1)
a = lk.LinkedList()
a.append_node(n1)
a.append_node(n2)
b = a.get_head()
c = b.get_next()
a.append_node(n3)
print('list 1')
a.percorror_linked()
print('list 2')
a.percorror_linked()
print('list emtpy')
a.clear_all()
a.percorror_linked()
'''
a.clear_all()
print('list all')
a.percorror_linked()
'''

