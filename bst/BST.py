class BST():
    """
    BST tree implemantation
    Attributes:
            root: first node in BST tree
    """
    def __init__(self):
        self.root = None
    
    def populate_root(self,node):
        """
        Populate the first bst's node(root)

        Args:
            node: a node that contains a values
        """
        if(self.root == None):
            self.root = node
        else:
            raise Exception('Root not empty')
            return
    
    def add_node(self,node):
        """
        Function to add nodes into the bst tree. 
        Works like any bst tree:
        
            left values < root.value
            rigth values > root.value

        Args:
            node: a node that contains a values
        """
        prev = None
        actual = self.root
        algo = None

        while True:
            if(actual == None):
                break

            elif(actual.get_value() == node.get_value()):
                raise Exception('Equals node')
                

            elif(actual.get_value() > node.get_value()):
                prev = actual
                actual = actual.get_left()
                algo = 'left'
                

            elif(actual.get_value() < node.get_value()):
                prev = actual
                actual = actual.get_rigth()
                algo = 'rigth'

        
        #actual now is the node        
        
        actual = node
        
        #his dad is his previous
        
        actual.prev = prev

        #his father now have the reference for him as left 
        if(algo == 'left'):
            prev.left = actual
        else:
            prev.rigth = actual

        