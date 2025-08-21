"""
Binary Search Tree (BST) with insert, search, and delete.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root.key
            yield from self.inorder(root.right)

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Found node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def min_value_node(self, node):
        while node.left:
            node = node.left
        return node

if __name__ == "__main__":
    bst = BST()
    root = None
    for val in [50, 30, 70, 20, 40, 60, 80]:
        root = bst.insert(root, val)

    print("In-order:", list(bst.inorder(root)))
    print("Search 40:", bst.search(root, 40) is not None)
    root = bst.delete(root, 20)
    print("After delete 20:", list(bst.inorder(root)))
