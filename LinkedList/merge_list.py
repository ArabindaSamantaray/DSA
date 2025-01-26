"""
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_list(head1, head2):
    if head1==None and head2==None:
        return None
    elif head1==None:
        return head2
    elif head2==None:
        return head1
    else:
        if head1.value<=head2.value:
            result=head1
            result.next = merge_list(head1.next, head2)
        else:
            result=head2
            result.next = merge_list(head1, head2.next)
        return result


def traverse(head):
    while head!=None:
        print(head.value)
        head=head.next

a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.next=c

w=Node(5)
x=Node(25)
y=Node(35)
z=Node(105)

w.next=x
x.next=y
y.next=z

traverse(merge_list(a,w))
