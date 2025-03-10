"""
Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

Do this in-place.

You may assume that the input list is non-empty.

You may assume that the input list contains the target.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_node(head, target):
    prev=head
    temp=head
    if head.value==target:
        return head.next
    while temp!=None:
        if temp.value==target:
            prev.next = temp.next
            temp.next=None
            return head
        temp = temp.next

def traverse(head):
    print("Remainin list")
    while head!=None:
        print(head.value)
        head = head.next

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

traverse(remove_node(a, "c"))

x = Node("x")
y = Node("y")
z = Node("z")

x.next = y
y.next = z
traverse(remove_node(x, "z"))

q = Node("q")
r = Node("r")
s = Node("s")

q.next = r
r.next = s
traverse(remove_node(q, "q"))


node1 = Node("h")
node2 = Node("i")
node3 = Node("j")
node4 = Node("i")

node1.next = node2
node2.next = node3
node3.next = node4
traverse(remove_node(node1, "i"))

t = Node("t")
traverse(remove_node(t, "t"))
