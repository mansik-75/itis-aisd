from node import Node
from queue import Queue
from stack import Stack
from random import randint

stack = Stack()

for _ in range(5):
    stack.push(Node(randint(1, 10)))

cur = stack.head
while cur:
    print(cur, end='  ')
    cur = cur.next

print()

for _ in range(5):
    print(stack.pop())



#########################################

queue = Queue()

for _ in range(5):
    queue.enqueue(Node(randint(1, 10)))

cur = queue.head
while  cur:
    print(cur, end='  ')
    cur = cur.next

print()
print(queue.check())
print()

for _ in range(5):
    print(queue.dequeue())
