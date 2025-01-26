"""
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.
"""


class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

def sum_list(head):
    sum_of_value = 0
    while head!=None:
        sum_of_value = sum_of_value+head.value
        head=head.next
    return sum_of_value


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

print(sum_list(a)==19)


x = Node(38)
y = Node(4)
x.next = y

print(sum_list(x)==42)

z = Node(100)
print(sum_list(z)==100)

print(sum_list(None)==0)
