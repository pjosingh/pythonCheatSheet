class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insertion in a binary search tree (BST)
def insert(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value)
    inorder(root.right)

root = None

root = insert(root, 3)
root = insert(root,10)
root = insert(root, 5)
root = insert(root, 1)

print(root)

inorder(root)


