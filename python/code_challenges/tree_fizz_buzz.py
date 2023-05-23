from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):
    if tree.root is None:
        return None


def fb_helper(value):
    if value % 15 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return str(value)
