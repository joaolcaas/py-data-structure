class nodeBST:
    """
    
    Node BST implemantation
    
        Attributes:
            value: node's value
            prev: previous node
            rigth: node at his rigth
            left: node at his left
    """

    def __init__(self, value):
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


class BST:
    """
    BST tree implemantation
    Attributes:
            root: first node in BST tree
    """

    def __init__(self):
        self.root = None

    def add_node(self, value):
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
            if actual == None:
                actual = nodeBST(value)
                actual.prev = prev

                if prev == None:
                    self.root = nodeBST(value)

                elif value < prev.get_value():
                    prev.left = actual
                else:
                    prev.rigth = actual

                break

            elif actual.get_value() == value:
                return "Equals node"

            elif actual.get_value() > value:
                prev = actual
                actual = actual.get_left()

            elif actual.get_value() < value:
                prev = actual
                actual = actual.get_rigth()

    def is_empty(self):
        """
            Check if bst tree has elements
        """

        if self.root == None:
            return True
        else:
            return False

    def search(self, value):
        """
        Search for a value into a created BST
        Args:
            value: a node value to search in BST
        """

        actual = self.root

        if actual == None:
            raise Exception("BST is empty")
            return

        while True:
            if actual == None:
                return "Searched value not found"
                break

            elif actual.get_value() == value:
                return actual.get_value()
                break

            elif value > actual.get_value():
                actual = actual.get_rigth()

            elif value < actual.get_value():
                actual = actual.get_left()

    def predecessor(self, node):
        """
        Search for a predecessor from a node.
            Predecessor will the higher value at the left node's subtree
        Args:
            node: a node that contains a values
        """

        actual = node

    def delete_node(self, value):
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

        if actual == None:
            raise Exception("BST is empty")
            return

        while True:

            if actual == None:
                # There is no value
                raise Exception("Value not found")
                return

            elif actual.get_value() == value:
                # achou o valor
                break

            elif actual.get_value() > value:
                # vai para a esquerda
                prev = actual
                actual = actual.get_left()

            elif actual.get_value() < value:
                # vai para a direita
                prev = actual
                actual = actual.get_rigth()

        left_chil = actual.left
        rigth_chil = actual.rigth

        # leaf node
        if left_chil == None and rigth_chil == None:
            # root case
            if prev == None:
                self.root = None
            else:
                if value < prev.get_value():
                    prev.left = None
                else:
                    prev.rigth = None

        # left node is not empty
        elif left_chil != None and rigth_chil == None:
            # root case
            if prev == None:
                self.root = left_chil
            else:
                prev.left = left_chil
                actual.prev = prev

        # rigth node is not empty
        elif left_chil == None and rigth_chil != None:
            # root case
            if prev == None:
                self.root = rigth_chil
            else:
                prev.rigth = rigth_chil
                actual.prev = prev

        # has two childnres
        # elif(left_chil != None and rigth_chil != None):

    def max_node(self):
        """
        Return the max value in BST
            (The depest children at BST rigth)
        """

        max = self.root

        if actual == None:
            raise Exception("BST is empty")
            return

        while actual.get_rigth() != None:
            actual = actual.get_rigth()

        return actual

    def min_node(self):
        """
        Return the min value in BST
            (The depest children at BST left)
        """

        min = self.root

        if actual == None:
            raise Exception("BST is empty")
            return

        while actual.get_left != None:
            actual = actual.get_left()

        return actual
