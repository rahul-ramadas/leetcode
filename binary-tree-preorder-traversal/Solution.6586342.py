class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []

        node = root
        node.parent = None
        preorderList = []

        while (node is not None):
            preorderList.append(node.val)

            if node.left is not None:
                node.left.parent = node
                node = node.left
                continue

            if node.right is not None:
                node.right.parent = node
                node = node.right
                continue

            while node.parent is not None and (node.parent.right is node or node.parent.right is None):
                node = node.parent
            node = node.parent

            if node is not None:
                node.right.parent = node
                node = node.right

        return preorderList
