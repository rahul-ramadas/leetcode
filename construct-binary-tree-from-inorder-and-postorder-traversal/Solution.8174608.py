class Solution:

    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        root_val = postorder[-1]
        index = inorder.index(root_val)
        left_tree = self.buildTree(inorder[:index], postorder[:index])
        right_tree = self.buildTree(inorder[index + 1:], postorder[index:-1])
        root = TreeNode(root_val)
        root.left = left_tree
        root.right = right_tree

        return root
