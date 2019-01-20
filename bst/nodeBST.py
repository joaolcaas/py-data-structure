class nodeBST:
    """
    
    Node BST implemantation
    
        Attributes:
            value: node's value
            prev: previous node
            rigth: node at his rigth
            left: node at his left
    """
    
    def __init__(self,value):
        """
            Args:
                value: node integer values

        """
        self.value = value
        self.prev = None
        self.rigth = None
        self.left = None
    
    def get_value(self):
        """
        Return a bstNode value
        """

        return self.value
    
    def get_left(self):
        """
        Return a bstNode left node
        """

        return self.left

    def get_rigth(self):
        """
        Return a bstNode rigth node
        """

        return self.rigth
    
    def get_previous(self):
        """
        Return a bstNode previous node
        """
        return self.prev