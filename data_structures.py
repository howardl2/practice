class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def get_value(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def __str__(self):
        s = "head"
        nextNode = self.head
        while nextNode:
            s += "->" + str(nextNode.value)
            nextNode = nextNode.next
        return s
