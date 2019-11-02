from SimpleNode import SimpleNode as no


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        if self.head != None:
            return self.head

    def append_node(self, value):
        if self.head == None:
            self.head = no(value)
        else:
            node = self.get_head()
            while node.has_next():
                node = node.get_next()
            node.set_next(no(value))

    def delete_node(self, value):
        if self.head == None:
            raise Exception("None head")
            return
        elif self.head.get_value() == value:
            aux = self.head.get_next()
            self.head.set_next(None)
            self.head = aux
        else:
            node = self.get_head()
            aux_next = self.get_head().get_next()
            aux_2_next = self.get_head().get_next().get_next()
            while aux_next.has_next():
                if aux_next.get_value() == value:
                    node.set_next(aux_2_next)
                    aux_next.set_next(None)
                    break
                else:
                    node = node.get_next()
                    aux_next = aux_next.get_next()
                    aux_2_next = aux_2_next.get_next()

    def clear_all(self):
        if self.head == None:
            print("Empty Linked list")
        else:
            self.head = None
            """
            if(self.head.get_value() != None):
                self.delete_node(self.head.get_value())
                self.clear_all()
            else:
                return self
            """

    def percorror_linked(self):
        head = self.get_head()
        if head != None:
            node = head
            print(node.get_value())
            while node.has_next():
                node = node.get_next()
                print(node.get_value())
        else:
            print("Empty Linked")

    def linked_list_len(self):
        head = self.get_head()
        if head == None:
            return 0
        else:
            final_len = 1
            node = head
            while node.has_next():
                final_len += 1
                node = node.get_next()
            return final_len

    def findMin(self):
        head = self.get_head()
        if head == None:
            return 0
        else:
            node = head
            min = node.get_value()
            while node.has_next():
                if node.get_next().get_value() < min:
                    min = node.get_next().get_value()
                node = node.get_next()
            return min

    def findMax(self):
        head = self.get_head()
        if head == None:
            return 0
        else:
            node = head
            min = node.get_value()
            while node.has_next():
                if node.get_next().get_value() > min:
                    min = node.get_next().get_value()
                node = node.get_next()
            return min

    def isEmpty(self):
        head = self.get_head()
        if head == None:
            return True
        return False

    def copy(self):
        head = self.get_head()
        if head == None:
            return None
        else:
            linked_copy = self
            return linked_copy

    def tostring(self):
        head = self.get_head()
        if head == None:
            print("Empty Linked")
        else:
            node = head
            count = 1
            out = (
                "position: "
                + str(count)
                + " "
                + "value: "
                + str(node.get_value())
                + "\n"
            )
            while node.has_next():
                count += 1
                out += (
                    "position: "
                    + str(count)
                    + " "
                    + "value: "
                    + str(node.get_next().get_value())
                    + "\n"
                )
                node = node.get_next()
        return out
