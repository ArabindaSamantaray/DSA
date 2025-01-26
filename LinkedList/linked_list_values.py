"""
Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.
"""

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

def contained_values(head):
    result = []
    while head!=None:
        result.append(head.value)
        head=head.next
    return result

def create_linked_list(list_of_values):
    head = Node(None)
    temp = head
    for value in list_of_values:
        node = Node(value)
        temp.next = node
        temp=node
    return contained_values(head.next)




print(create_linked_list([ 'a', 'b', 'c', 'd' ]))
print(create_linked_list([ 'x', 'y' ]))
print(create_linked_list([ 'q' ]))

