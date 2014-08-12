class Solution:
    def getBSTForRange(self, num, left, right):
        if left == right:
            return None

        middle = (left + right) // 2
        root = TreeNode(num[middle])
        root.left = self.getBSTForRange(num, left, middle)
        root.right = self.getBSTForRange(num, middle + 1, right)
        return root

    def sortedArrayToBST(self, num):
        return self.getBSTForRange(num, 0, len(num))
