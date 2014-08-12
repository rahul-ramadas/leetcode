class Solution:
    def maxBalancedHeight(self, root):
        if root is None:
            return 0

        leftHeight = self.maxBalancedHeight(root.left)
        rightHeight = self.maxBalancedHeight(root.right)
        if leftHeight == -1 or rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root):
        return self.maxBalancedHeight(root) != -1
