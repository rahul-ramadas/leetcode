class Solution:

    @staticmethod
    def next_path_sum(root, sum):
        if root.left is None and root.right is None and root.val == sum:
            yield [root.val]
        else:
            if root.left:
                for path in Solution.next_path_sum(root.left, sum - root.val):
                    yield [root.val] + path
            if root.right:
                for path in Solution.next_path_sum(root.right, sum - root.val):
                    yield [root.val] + path

    def pathSum(self, root, sum):
        if root is None:
            return []

        return [path for path in self.next_path_sum(root, sum)]
