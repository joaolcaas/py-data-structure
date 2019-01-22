from nodeBST import nodeBST
class BST():
    """
    BST tree implemantation
    Attributes:
            root: first node in BST tree
    """
    def __init__(self):
        self.root = None
    
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
                actual = nodeBST(value)
                actual.prev = prev
                
                if(prev == None):
                    self.root = nodeBST(value)

                elif(value < prev.get_value()):
                    prev.left = actual
                else:
                    prev.rigth = actual

                break

            elif(actual.get_value() == value):
                raise Exception('Equals node')
                
            elif(actual.get_value() > value):
                prev = actual
                actual = actual.get_left()
                
            elif(actual.get_value() < value):
                prev = actual
                actual = actual.get_rigth()

    
    def is_empty(self):
        """
            Check if bst tree has elements
        """

        if(self.root == None):
            return True
        else:
            return False

    def search(self,value):
        
    def predecessor(self,node):

    def delete_node(self,value):
        """
        Rules:
            If is a leaf, just delete (left = none and rigth = none)
            Node has one childrem: 
                No rigth child: set parent of deleted node to left child of deleted node
                No left child: set parent of deleted node to left child of deleted node
            Node has two childrens -> find the largest in left subtree and turn it the new node
            
            Args:
            
        """

        prev = None
        actual = self.root

        if(actual == None):
            raise Exception("BST is empty")
            return 

        while True:
            
            if(actual == None):
                #There is no value
                raise Exception("Value not found")
                return 

            elif(actual.get_value() == value):
                #achou o valor
                break

            elif(actual.get_value() > value):
                #vai para a esquerda
                prev = actual
                actual = actual.get_left()

            elif(actual.get_value() < value):
                #vai para a direita
                prev = actual
                actual = actual.get_rigth()
        
        left_chil = actual.left
        rigth_chil = actual.rigth
        
        #leaf node
        if(left_chil == None and rigth_chil == None):
            #root case
            if(prev == None):
                self.root = None
            else:
                if(value < prev.get_value()):
                    prev.left = None
                else:
                    prev.rigth = None
        
        #left node is not empty
        elif(left_chil != None and rigth_chil == None):
            #root case
            if(prev == None):
                self.root = left_chil
            else:
                prev.left = left_chil
                actual.prev = prev

        #rigth node is not empty 
        elif(left_chil == None and rigth_chil != None):
            #root case
            if(prev == None):
                self.root = rigth_chil
            else:
                prev.rigth = rigth_chil
                actual.prev = prev

        #has two childnres
        elif(left_chil != None and rigth_chil != None):
        

