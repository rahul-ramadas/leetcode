class Stack:

    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        del self.stack[-1]


class Queue:

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def push(self, x):
        self.prepare_for_push()
        self.push_stack.push(x)

    def pop(self):
        self.prepare_for_pop()
        self.pop_stack.pop()

    def peek(self):
        self.prepare_for_pop()
        return self.pop_stack.peek()

    def prepare_for_push(self):
        if self.pop_stack.empty():
            return

        while not self.pop_stack.empty():
            self.push_stack.push(self.pop_stack.peek())
            self.pop_stack.pop()

    def prepare_for_pop(self):
        if self.push_stack.empty():
            return

        while not self.push_stack.empty():
            self.pop_stack.push(self.push_stack.peek())
            self.push_stack.pop()

    def empty(self):
        return self.push_stack.empty() and self.pop_stack.empty()
