class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = 0

    def push(self, x):
        if not self.stack:
            self.current_min = x
            self.stack.append(0)
            return

        diff = x - self.current_min
        if diff < 0:
            self.current_min = x
        self.stack.append(diff)

    def pop(self):
        diff = self.stack.pop()
        if diff < 0:
            self.current_min = self.current_min - diff

    def top(self):
        diff = self.stack[-1]
        if diff < 0:
            return self.current_min
        return self.current_min + diff

    def getMin(self):
        return self.current_min
