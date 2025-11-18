# Task_1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
class UnsortedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} is not in the list")

    def pop(self, index=None):
        if not self.head:
            raise IndexError("pop from empty list")

        if index is None:
            index = self.size - 1
        if index < 0 or index >= self.size:
            raise IndexError("pop index out of range")

        if index == 0:
            popped = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped

        current = self.head
        for _ in range(index - 1):
            current = current.next
        popped = current.next.data
        current.next = current.next.next
        self.size -= 1
        return popped

    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("insert index out of range")

        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def slice(self, start, stop):
        if start < 0 or stop > self.size or start > stop:
            raise IndexError("slice indices out of range")

        result = UnsortedList()
        current = self.head
        for _ in range(start):
            current = current.next
        for _ in range(start, stop):
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"


# Task_2

def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

