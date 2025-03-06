"""
Create a BST

# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root==None:
        return Node(value)
    elif value<=root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def bfs_traversal(root):
    queue=[root]
    result =[]
    while len(queue)!=0:
        node = queue.pop(0)
        result.append(node.value)
        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)
    return result

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

print(bfs_traversal(root)==[50, 30, 70, 20, 40, 60, 80])
