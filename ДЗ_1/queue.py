from node import Node


class Queue:
    length = 0
    head = None
    tail = None

    def enqueue(self, node: Node):
        self.head, node.next = node, self.head
        if self.length == 0:
            self.tail = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise Exception('You try to dequeu empty queue')

        if self.length == 1:
            last = self.head
            self.head, self.tail = None, None
            self.length -= 1
            return last

        current = self.head
        while current.next.next:
            current = current.next

        last = current.next
        current.next = None
        self.tail = current
        self.length -= 1

        return last

    def check(self):
        if self.length == 0:
            raise Exception('You try to check empty queue')
        return self.tail.value

    def len(self):
        return self.length
