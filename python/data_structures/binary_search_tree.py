from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root

        while current:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def contains(self, value):
        if self.root is None:
            return False

        current = self.root

        while current is not None:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right

        return False



