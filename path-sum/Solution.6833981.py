class Solution:

    def hasPathSum(self, root, sum):
        if root is None:
            return False

        root.path_sum = root.val
        process = collections.deque([root])

        while process:
            node = process.popleft()
            if node.left is None and node.right is None:
                if node.path_sum == sum:
                    return True
                continue

            if node.left is not None:
                node.left.path_sum = node.path_sum + node.left.val
                process.append(node.left)

            if node.right is not None:
                node.right.path_sum = node.path_sum + node.right.val
                process.append(node.right)

        return False
