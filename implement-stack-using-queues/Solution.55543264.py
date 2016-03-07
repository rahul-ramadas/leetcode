class Queue:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.popleft()

    def front(self):
        return self.queue[0]

    def empty(self):
        return True if len(self.queue) == 0 else False

    def __len__(self):
        return len(self.queue)


class Stack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x):
        self.queue.push(x)

    def pop(self):
        n = len(self.queue)
        for i in xrange(n - 1):
            self.queue.push(self.queue.pop())
        return self.queue.pop()

    def top(self):
        t = self.pop()
        self.push(t)
        return t

    def empty(self):
        return self.queue.empty()
