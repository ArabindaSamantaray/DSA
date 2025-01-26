"""
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
"""

class Node:
    def  __init__(self, value):
        self.value = value
        self.next = None

def zipper_lists(head1, head2):
    if head1==None and head2==None:
        return None
    elif head1==None:
        return head2
    elif head2==None:
        return head1
    else:
        result = head1
        result.next=zipper_lists(head2, head1.next)
        return result


def traverse(head):
    while head!=None:
        print(head.value)
        head=head.next












a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

traverse(zipper_lists(a, x))
