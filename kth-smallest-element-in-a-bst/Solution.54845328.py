# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.insert_counts(root)
        return self.find_kth_smallest(root, k)
        
    def find_kth_smallest(self, root, k):
        while True:
            left_count = root.left.count if root.left is not None else 0
            right_count = root.right.count if root.right is not None else 0
        
            if left_count == k - 1:
                return root.val
        
            if left_count >= k:
                root = root.left
            else:
                k -= left_count + 1
                root = root.right
        
    def insert_counts(self, root):
        if root is None:
            return
        
        self.insert_counts(root.left)
        self.insert_counts(root.right)
        
        root.count = 1
        root.count += root.left.count if root.left is not None else 0
        root.count += root.right.count if root.right is not None else 0
