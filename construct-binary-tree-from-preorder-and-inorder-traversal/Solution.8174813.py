class Solution:

    def buildTree(self, preorder, inorder):
        if not inorder:
            return None

        root_val = preorder[0]
        index = inorder.index(root_val)
        left_tree = self.buildTree(preorder[1:index + 1], inorder[:index])
        right_tree = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        root = TreeNode(root_val)
        root.left = left_tree
        root.right = right_tree

        return root
