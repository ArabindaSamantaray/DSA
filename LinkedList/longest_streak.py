"""
Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def longest_streak(head):
    if head==None:
        return 0
    prev_value = head.value
    max_streak_length = float("-inf")
    current_streak_length = 0
    while head!=None:
        if head.value==prev_value:
            current_streak_length = current_streak_length+1
        else:
            if current_streak_length>max_streak_length:
                max_streak_length = current_streak_length
            current_streak_length = 1
            prev_value = head.value
        head = head.next
    if current_streak_length>max_streak_length:
        max_streak_length = current_streak_length
    return max_streak_length







a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print(longest_streak(a)==3)

a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print(longest_streak(a)==4)

a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print(longest_streak(a)==3)

a = Node(5)
b = Node(5)

a.next = b
print(longest_streak(a)==2)

a = Node(4)
print(longest_streak(a)==1)

print(longest_streak(None)==0)
