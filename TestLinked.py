from structure import LinkedList as lk
from structure import SimpleNode as no


n1 = no.SimpleNode(130)
n2 = no.SimpleNode(2)
n3 = no.SimpleNode(11)
a = lk.LinkedList()
a.append_node(n1)
er = a.isEmpty()
print er
b = a.findMin()
print('menor')
print(b)
print('--------')
a.append_node(n2)
a.percorror_linked()
c = a.findMin()
print('menor')
print(c)
b = a.get_head()
c = b.get_next()
a.append_node(n3)
print('list 1')
a.percorror_linked()
print('list 2')
a.percorror_linked()
print('list emtpy')
#a.clear_all()
a.percorror_linked()
d = a.findMax()
print d
copy = a.copy()
print('linked a')
a.percorror_linked()
print('linked copy')
copy.percorror_linked()


