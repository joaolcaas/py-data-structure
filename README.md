# py-linked-list
Implemented linked list in python

**To do**
```sh
    Criar class Node; (OK)
    Criar métodos para a linked list funcionar: (OK)
        - addToStart
        - pop() : pop method removes last element of the Linked List
        - search
        - reverse() : method that returns reversed linked list
        - sort
    Criar módulo pip install
    Criar mais estururas (double, stack, queue)
    
```

**Usage**
- Simple Linked List

```sh
    To create a linked list (no order):
        from structure import LinkedList as lk

        my_linked = lk.LinkedList()
    
    Populate with nodes:
        from structure import SimpleNode as no

        node1 = no.SimpleNode(1)
        my_linked.append_node(node1)
    
    Delete a node:

        my_linked.delete_node(node1)
    
    Clear the all linked list:

        my_linked.clear_all()
    
```