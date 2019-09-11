class ListNode:
    """A linked list as represented on LeetCode"""
    def __init__(self, x, nextNode=None):
        self.val = x
        self.next = nextNode
    
    def asInt(self):
        nextNode = self.next
        total = str(self.val)
        while nextNode:
            total = str(nextNode.val) + total
            nextNode = nextNode.next
        return int(total)

    def __str__(self):
        s = "->" + str(self.val)
        nextNode = self.next
        while nextNode:
            s += "->" + str(nextNode.val)
            nextNode = nextNode.next
        return s

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




class DirectedGraphNode(object):
    """Represent a directed graph"""
    def __init__(self, value, edges_in=[], edges_out=[]):
        self.edges_in = edges_in
        self.edges_out = edges_out
        self.value = value
