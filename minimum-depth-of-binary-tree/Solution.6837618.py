class Solution:

    def minDepth(self, root):
        if root is None:
            return 0

        process = collections.deque([(root, 1)])

        while process:
            node, depth = process.popleft()
            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                process.append((node.left, depth + 1))
            if node.right is not None:
                process.append((node.right, depth + 1))
