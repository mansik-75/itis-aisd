from node import Node


class Stack:
    length = 0
    head = None

    def isEmpty(self):
        return self.head is None

    def push(self, node: Node):
        self.head, node.next = node, self.head
        self.length += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('You try to pop from empty stack')
        first_elem = self.head
        self.head = self.head.next
        self.length -= 1

        return first_elem

    def peek(self):
        return self.head.value
