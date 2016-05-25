# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def get_height(self, root):
        node = root
        height = 0
        while node is not None:
            height += 1
            node = node.left
        return height

    def countNodes(self, root):
        if root is None:
            return 0

        h = self.get_height(root)
        node = root
        count = 0
        
        while node is not None:
            h -= 1
            count += 1
            if self.get_height(node.right) == h:
                count += (2 ** h) - 1
                node = node.right
            else:
                count += (2 ** (h - 1)) - 1
                node = node.left
        
        return count
