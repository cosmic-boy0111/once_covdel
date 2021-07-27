#First in last out rule is followed in queue
#queue is also called as producer consumer problem
from collections import deque

class HyperStanQueue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

orderqueue = HyperStanQueue()