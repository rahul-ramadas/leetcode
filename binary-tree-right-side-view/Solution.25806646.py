# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def post_fix(self, root, level=0):
        if root is None:
            return

        self.post_fix(root.left, level + 1)
        self.post_fix(root.right, level + 1)
        
        self.level_map[level] = root.val
        
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        self.level_map = dict()
        
        self.post_fix(root)
        
        level_list = [self.level_map[i] for i in xrange(len(self.level_map))]
        return level_list
