class SimpleNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        """
        Return a node Value
        """
        return self.value

    def get_next(self):
        """
        Return the next node or None
        """
        return self.next

    def set_next(self, node):
        """
        Set a the next node Value
        """
        self.next = node
        return self

    def has_next(self):
        if self.get_next() != None:
            return True
        return False
