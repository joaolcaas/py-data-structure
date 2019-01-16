class BST():
    def __init__(self):
        self.root = None
    
    def populate_root(self,node):
        if(self.root != None):
            self.root == node
        else:
            raise Exception('Root not empty')
            return