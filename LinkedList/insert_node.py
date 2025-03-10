"""
Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the length of the input list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_node(head, value, index):
    if index == 0:
        node = Node(value)
        node.next = head
        return node
    head.next = insert_node(head.next, value, index-1)
    return head

def traverse(head):
    print("New list")
    while head!=None:
        print(head.value)
        head = head.next





a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d
traverse(insert_node(a, 'x', 2))


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d
traverse(insert_node(a, 'v', 3))

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d
traverse(insert_node(a, 'm', 4))


a = Node("a")
b = Node("b")

a.next = b
traverse(insert_node(a, 'z', 0))
