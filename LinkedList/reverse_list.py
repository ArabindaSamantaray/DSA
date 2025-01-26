"""
Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def traverse(head):
    while head!=None:
        print(head.value)
        head=head.next


def reverse_list_iterative(head):
    prev = None
    temp = head
    while temp.next!=None:
        temp1 = temp.next
        temp.next = prev
        prev = temp
        temp = temp1
    temp.next = prev
    return temp




print("Iterative")
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

traverse(reverse_list_iterative(a))

print("Recursive")
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

traverse(reverse_list_recursive(a))
