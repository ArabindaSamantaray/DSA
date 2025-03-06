"""
Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first(root):
    result = []
    if root!=None:
        queue=[root]
        while len(queue)!=0:
            node = queue.pop(0)
            result.append(node.value)
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
    return result

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
print(breadth_first(a)==['a', 'b', 'c', 'd', 'e', 'f'])


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

print(breadth_first(a)==['a', 'b', 'c', 'd', 'e', 'f', 'g'])


a = Node('a')
print(breadth_first(a)==['a'])

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')
a.right = b;
b.left = c;
c.left = x;
c.right = d;
d.right = e;
print(breadth_first(a)==['a', 'b', 'c', 'x', 'd', 'e'])

print(breadth_first(None)==[])
