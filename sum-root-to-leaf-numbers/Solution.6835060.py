class Solution:

    def sumNumbers(self, root):
        if root is None:
            return 0

        solution = 0
        root.path_number = root.val
        process = collections.deque([root])

        while process:
            node = process.popleft()
            if node.left is None and node.right is None:
                solution += node.path_number
                continue

            if node.left is not None:
                node.left.path_number = node.path_number * 10 + node.left.val
                process.append(node.left)

            if node.right is not None:
                node.right.path_number = node.path_number * 10 + node.right.val
                process.append(node.right)

        return solution
