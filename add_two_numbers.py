# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
from data_structures import ListNode

def add_two_numbers(l1, l2): # O(N)
    currNode1, currNode2 = l1, l2
    nextNode1, nextNode2 = l1, l2
    headNode = ListNode(None)
    currRetNode = headNode
    carry = 0
    while nextNode1 or nextNode2 or carry:
        currRetNode.next = ListNode(0)
        currRetNode = currRetNode.next
        currNode1 = nextNode1
        currNode2 = nextNode2
        n1, n2 = 0, 0
        if currNode1:
            n1 = currNode1.val
            nextNode1 = currNode1.next
        if currNode2:
            n2 = currNode2.val
            nextNode2 = currNode2.next
        added = n1 + n2 + carry
        carry = 0
        if added >= 10:
            added -= 10
            carry = 1
        currRetNode.val = added
    return headNode.next


l1 = ListNode(3, ListNode(4, ListNode(2)))
l2 = ListNode(4, ListNode(6, ListNode(5)))

# print(add_two_numbers(l1,l2) == 243 + 564)
print(add_two_numbers(l1,l2).asInt() == 243 + 564)

l1 = ListNode(3, ListNode(4))
l2 = ListNode(4, ListNode(6, ListNode(5)))

print(add_two_numbers(l1,l2).asInt() == 43 + 564)

l1 = ListNode(0)
l2 = ListNode(4, ListNode(6, ListNode(5)))

print(add_two_numbers(l1,l2).asInt() == 0 + 564)

l1 = ListNode(0)
l2 = ListNode(0)

print(add_two_numbers(l1,l2).asInt() == 0)

l1 = ListNode(0, ListNode(4))
l2 = ListNode(4, ListNode(6, ListNode(5, ListNode(7))))

print(add_two_numbers(l1,l2).asInt() == 40 + 7564)

l1 = ListNode(5)
l2 = ListNode(5)

print(add_two_numbers(l1,l2).asInt() == 5 + 5)