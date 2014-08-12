class Solution:

    def postorderTraversal(self, root):
        if root is None:
            return []

        traversal = []

        root.parent = None
        node = root
        while node is not None:
            while (node.left is not None or node.right is not None):
                if node.left is not None:
                    node.left.parent = node
                    node = node.left
                elif node.right is not None:
                    node.right.parent = node
                    node = node.right

            while node is not None:
                if node.right is not None and not hasattr(node.right, 'parent'):
                    node.right.parent = node
                    node = node.right
                    break

                traversal.append(node.val)
                node = node.parent

        return traversal
