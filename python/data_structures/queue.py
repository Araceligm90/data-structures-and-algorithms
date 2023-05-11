from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        # dequeue the first element in the queue by retrieving the value of the front node (value = self.front.value)
        # and updating the front node to be the next node in the queue (self.front = self.front.next).
        value = self.front.value
        self.front = self.front.next

        return value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

