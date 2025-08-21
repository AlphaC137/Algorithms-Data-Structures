"""
Binary Tree with basic traversals (in-order, pre-order, post-order).
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)

    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.key
            yield from self.inorder(node.right)

    def preorder(self, node):
        if node:
            yield node.key
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)

    def postorder(self, node):
        if node:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node.key

if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("In-order:", list(tree.inorder(tree.root)))
    print("Pre-order:", list(tree.preorder(tree.root)))
    print("Post-order:", list(tree.postorder(tree.root)))
