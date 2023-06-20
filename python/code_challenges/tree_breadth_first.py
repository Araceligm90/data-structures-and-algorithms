from collections import deque

# Completed this code with the help of ChatGPT, that suggested to use a deque for an efficient queue implementation


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


def breadth_first(tree):
    if tree.root is None:
        return []

    queue = deque([tree.root])
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return traversal
