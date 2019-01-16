# py-data-sturcture
Implemented structures in python

**Structures**
```sh
    - LinkedList
    - DoubleLinkedList
    - BST
```
**To do**
```sh
    
    New methods (LinkedList): 
        - addToStart
        - pop() : pop method removes last element of the Linked List
        - search
        - reverse() : method that returns reversed linked list
        - sort
    New methods (DoubleLinkedList):


    Create more structures (double, stack, queue)

    
```

**Usage**
- Simple Linked List

```sh
    To create a linked list (no order):
       from linkedList import LinkedList as lk

        my_linked = lk.LinkedList()
    
    Populate with nodes:
        from linkedList import SimpleNode as no

        node1 = no.SimpleNode(1)
        my_linked.append_node(node1)
    
    Delete a node:

        my_linked.delete_node(node1)
    
    Clear the all linked list:

        my_linked.clear_all()

    Show all linked lsit:
        my_linked.tostring()
    
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)