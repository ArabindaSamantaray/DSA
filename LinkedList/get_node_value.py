"""
Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_node_value(head, index):
    if head==None:
        return None
    if index==0:
        return head.value
    return get_node_value(head.next, index-1)







a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 2)=='c')

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 3)=='d')

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 7)==None)

node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

print(get_node_value(node1, 1)=='mango')
