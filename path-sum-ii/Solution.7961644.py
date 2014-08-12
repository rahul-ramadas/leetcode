class Solution:

    def pathSum(self, root, sum):
        if root is None:
            return []

        root.parent = None
        levels = collections.deque([(root, 0)])
        result = []

        while levels:
            node, sum_so_far = levels.popleft()

            if node.left is None and node.right is None and sum_so_far + node.val == sum:
                path = []
                while node:
                    path.append(node.val)
                    node = node.parent
                result.append(list(reversed(path)))
                continue

            if node.left:
                node.left.parent = node
                levels.append((node.left, sum_so_far + node.val))
            if node.right:
                node.right.parent = node
                levels.append((node.right, sum_so_far + node.val))

        return result
