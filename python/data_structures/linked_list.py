class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.next = old_head

    def __str__(self):
        # start with empty string
        text = ""
        # traverse my linked list

        # 1) Initialize a variable named current, set to head
        current = self.head
        # 2) Start a while loop, choose between current or current.next. In this case we are going for current as we
        # are visiting each nose
        while current:
            # 3) Do a thing - concatenating to the string 'text'
            text += f"{{ {current.value} }} -> "
            # 4) Move pointer for current
            current = current.next

        return text + "NULL"
    # dunder str always needs to return a string

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, new_value):
        current = self.head
        new_node = Node(new_value)

        if current is None:
            self.head = new_node
            return

        while current.next:
            current = current.next

        current.next = new_node

    def insert_before(self, target_value, new_value):
        current = self.head
        new_node = Node(new_value)

        if current is None:
            self.head = new_node
            return

        if current.value == target_value:
            self.insert(new_value)
            return

        while current.next:
            if current.next.value == target_value:
                new_node.next = new_node
                return
            current = current

    def insert_after(self, target_value, new_value):
        current = self.head
        new_node = Node(new_value)

        if current is None:
            self.head = new_node
            return

        while current:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def kth_from_end(self, k):
        if k < 0:
            raise ValueError('K cannot be a negative number')

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        if count == 0:
            raise ValueError('This list is empty')

        if k >= count:
            raise ValueError('K is greater than or equal to the number of nodes')

        current = self.head
        for _ in range(count - k - 1):
            current = current.next

        return current.value


class TargetError(Exception):
    pass
