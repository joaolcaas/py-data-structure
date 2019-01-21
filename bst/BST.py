from nodeBST import nodeBST
class BST():
    """
    BST tree implemantation
    Attributes:
            root: first node in BST tree
    """
    def __init__(self):
        self.root = None
    
    def populate_root(self,value):
        """
        Populate the first bst's node(root)

        Args:
            node: a node that contains a values
        """
        if(self.root == None):
            self.root = nodeBST(value)
        else:
            raise Exception('Root not empty')
            return
    
    def add_node(self,value):
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

        while True:
            if(actual == None):
                break

            elif(actual.get_value() == value):
                raise Exception('Equals node')
                

            elif(actual.get_value() > value):
                prev = actual
                actual = actual.get_left()
                
                

            elif(actual.get_value() < value):
                prev = actual
                actual = actual.get_rigth()
                

        
        #actual now is the node        
        
        actual = nodeBST(value)
        
        #his dad is his previous
        
        actual.prev = prev

        #his father now have the reference for him as left or rigth
        if(value < prev.get_value()):
            prev.left = actual
        else:
            prev.rigth = actual

    
    def delete_node(self,value):
        """
        Rules:
            If is a leaf, just delete (left = none and rigth = none)
            Node has one childrem: 
                No rigth child: set parent of deleted node to left child of deleted node
                No left child: set parent of deleted node to left child of deleted node
            Node has two childrens -> find the largest in left subtree and turn it the new node
            
        """