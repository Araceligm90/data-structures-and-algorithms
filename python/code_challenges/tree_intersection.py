from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    # Step 1: Create dictionaries to store values encountered in the trees
    tree1_values = {}
    intersection_set = set()

    # Step 2: Traverse the first binary tree and add values to the dictionary
    def traverse_tree1(node):
        if node is None:
            return
        tree1_values[node.value] = True
        traverse_tree1(node.left)
        traverse_tree1(node.right)

    traverse_tree1(tree1.root)  # Assuming the root of tree1 is accessible as tree1.root

    # Step 3: Traverse the second binary tree and check values in the dictionary
    def traverse_tree2(node):
        if node is None:
            return
        if node.value in tree1_values:
            intersection_set.add(node.value)
        traverse_tree2(node.left)
        traverse_tree2(node.right)

    traverse_tree2(tree2.root)  # Assuming the root of tree2 is accessible as tree2.root

    # Step 4: Return the intersection set
    return intersection_set
