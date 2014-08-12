class Solution:
    def isMirrorImage(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        return self.isMirrorImage(left.left, right.right) and \
            self.isMirrorImage(left.right, right.left)

    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirrorImage(root.left, root.right)
