class Solution:

    def postorderTraversal(self, root):
        traversal = []

        def do_traversal(node):
            if node is None:
                return

            do_traversal(node.left)
            do_traversal(node.right)
            traversal.append(node.val)

        do_traversal(root)
        return traversal
