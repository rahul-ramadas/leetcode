class BSTIterator:

    def __init__(self, root):
        self.iter = iter(BSTIterator.next_smallest(root))
        if root is None:
            self.done = True
        else:
            self.done = False
            self.next_element = next(self.iter).val

    def hasNext(self):
        return not self.done

    @staticmethod
    def next_smallest(node):
        if node is None:
            raise StopIteration
        for n in BSTIterator.next_smallest(node.left):
            yield n
        yield node
        for n in BSTIterator.next_smallest(node.right):
            yield n

    def next(self):
        try:
            result = self.next_element
            self.next_element = next(self.iter).val
        except StopIteration:
            self.done = True
        return result
