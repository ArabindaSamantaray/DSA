"""
Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_values(root):
    if root==None:
        return []
    else:
        return [root.value]+depth_first_values(root.left)+depth_first_values(root.right)



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(depth_first_values(a)==['a', 'b', 'd', 'e', 'c', 'f'])


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(depth_first_values(a)==['a', 'b', 'd', 'e', 'g', 'c', 'f'])


a = Node('a')
print(depth_first_values(a)==['a'])

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b;
b.left = c;
c.right = d;
d.right = e;
print(depth_first_values(a)==['a', 'b', 'c', 'd', 'e'])

print(depth_first_values(None)==[])
