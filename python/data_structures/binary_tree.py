class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        def traverse(node, result):
            # If node id not None, append its value to the result list and recursively call traverse on its left and
            # right child nodes
            if node is not None:
                result.append(node.value)
                traverse(node.left, result)
                traverse(node.right, result)

        # Initialize an empty list to accumulate the values
        result = []
        # Call the traverse function on the root node to perform the traversal
        traverse(self.root, result)
        return result

    def post_order(self):
        def traverse(node, result):
            if node is not None:
                traverse(node.left, result)
                traverse(node.right, result)
                result.append(node.value)

        result = []
        traverse(self.root, result)
        return result

    def in_order(self):
        def traverse(node, result):
            if node is not None:
                traverse(node.left, result)
                result.append(node.value)
                traverse(node.right, result)

        result = []
        traverse(self.root, result)
        return result

    def find_maximum_value(self):
        if not self.root:
            return None

        max_val = self.root.value

        def traverse(node):
            nonlocal max_val
            if not node:
                return

            if node.value > max_val:
                max_val = node.value

            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return max_val


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
