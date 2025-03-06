"""
Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def path_finder(root, target):
    path = _path_finder(root, target)
    if path:
        path.reverse()
        return path
    return None

def _path_finder(root, target):
    if root==None:
        return None
    elif root.value == target:
        return [target]
    else:
        left_path = _path_finder(root.left, target)
        right_path = _path_finder(root.right, target)
        if left_path!=None:
            left_path.append(root.value)
            return left_path
        elif right_path!=None:
            right_path.append(root.value)
            return right_path
        else:
            return None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(path_finder(a, 'e') == ['a', 'b', 'e'])


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(path_finder(a, 'p')==None)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

print(path_finder(a, "c")==['a', 'c'])


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
print(path_finder(a, "h")==['a', 'c', 'f', 'h'])


x = Node("x")
print(path_finder(x, "x")==['x'])

print(path_finder(None, "x")==None)
