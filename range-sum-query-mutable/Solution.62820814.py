class TreeNode:

    def __init__(self, begin, end):
        self.sum = 0
        self.left = None
        self.right = None
        self.parent = None
        self.begin = begin
        self.end = end


class NumArray:

    def __init__(self, nums):
        if nums:
            self.root = self.build(nums, 0, len(nums))

    def build(self, nums, begin, end):
        if begin == end:
            raise Exception

        root = TreeNode(begin, end)
        if end - begin == 1:
            root.sum = nums[begin]
        else:
            mid = (begin + end) / 2
            root.left = self.build(nums, begin, mid)
            root.right = self.build(nums, mid, end)
            root.left.parent = root
            root.right.parent = root
            root.sum = root.left.sum + root.right.sum
        return root

    def update(self, i, val):
        self.update_tree(self.root, i, val)

    def update_tree(self, root, i, val):
        if root.end - root.begin == 1:
            root.sum = val
            return

        if root.left.begin <= i < root.left.end:
            self.update_tree(root.left, i, val)
        else:
            self.update_tree(root.right, i, val)

        root.sum = root.left.sum + root.right.sum

    def sumRange(self, i, j):
        return self.sum_range(self.root, i, j + 1)

    def sum_range(self, root, begin, end):
        if root is None:
            return 0

        if root.begin >= begin and root.end <= end:
            return root.sum

        if root.begin >= end or root.end <= begin:
            return 0

        return self.sum_range(root.left, begin, end) + self.sum_range(root.right, begin, end)
