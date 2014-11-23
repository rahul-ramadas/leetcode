import unittest


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


class MinStackTest(unittest.TestCase):

    def test_push(self):
        any_number = 123
        stack = MinStack()
        stack.push(any_number)
        self.assertEqual(stack.top(), any_number)

    def test_pop(self):
        first_number = 123
        second_number = 456
        stack = MinStack()
        stack.push(first_number)
        stack.push(second_number)
        stack.pop()
        self.assertEqual(stack.top(), first_number)

    def test_min(self):
        numbers = [5, 8, 1, 3, 6]
        stack = MinStack()
        for number in numbers:
            stack.push(number)
        self.assertEqual(stack.getMin(), 1)


if __name__ == '__main__':
    unittest.main()
