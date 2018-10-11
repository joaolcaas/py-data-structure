# py-linked-list
Implemented linked list in python

**To do**
```sh
    Criar class Node;
    Criar métodos para a linked list funcionar:
        - Add node
        - Remove node 
        - Remove Head(Se quiser apagar o head, tem que setar o proximo do head como head)
        - Percorrer os nós(has_next())
        - Linked List ordenada
        - clear()
        - addLast()
        - pip install
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