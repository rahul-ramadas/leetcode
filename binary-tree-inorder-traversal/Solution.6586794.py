class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []

        node = root
        node.parent = None
        inorderList = []

        while node is not None:
            while node.left is not None:
                node.left.parent = node
                node = node.left
                continue

            inorderList.append(node.val)
            if node.right is not None:
                node.right.parent = node
                node = node.right
                continue

            while node.parent is not None:
                if node.parent.left is node:
                    node = node.parent
                    inorderList.append(node.val)
                    if node.right is not None:
                        node.right.parent = node
                        node = node.right
                        break
                else:
                    node = node.parent
            else:
                node = node.parent

        return inorderList