class LinkedList():
    def __init__(self):
        self.head = None
    
    def get_head(self):
        if(self.head != None):
            return self.head
        else:
            raise Exception('None head')
            return

    def append_node(self,new_node):
        if(self.head == None):
            self.head = new_node
        else:
            head = self.get_head()
            if(head != None):
                node = head
                while(node.has_next()):
                    node = node.get_next()
                node.set_next(new_node)
            else:
                raise Exception('Node Head node')
                return
    
    def percorror_linked(self):
        head = self.get_head()
        if(head != None):
            node = head
            print(node.get_value())
            while(node.has_next()):
                node = node.get_next()
                print(node.get_value())
        else:
            raise Exception('None head node')
            return

if __name__ == '__main__':
    LinkedList()