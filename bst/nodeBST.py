class nodeBST:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.rigth = None
        self.left = None
    
    def get_value(self):
        """
        Return a bstNode value
        """

        return self.value
    