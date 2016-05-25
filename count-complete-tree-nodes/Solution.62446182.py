# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def get_left_height(self, root):
        node = root
        height = 0
        while node is not None:
            height += 1
            node = node.left
        return height
        
    def get_right_height(self, root):
        node = root
        height = 0
        while node is not None:
            height += 1
            node = node.right
        return height
        
    def countNodes(self, root):
        if root is None:
            return 0

        left_h = self.get_left_height(root)
        right_h = self.get_right_height(root)
        
        if left_h == right_h:
            return (2 ** left_h) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
