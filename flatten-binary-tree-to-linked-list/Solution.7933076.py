class Solution:

    def flatten(self, root):
        while root:
            if root.left:
                node = root.left
                while True:
                    if node.right:
                        node = node.right
                    elif node.left:
                        node = node.left
                    else:
                        break
                node.right = root.right
                root.right = root.left
                root.left = None

            root = root.right
