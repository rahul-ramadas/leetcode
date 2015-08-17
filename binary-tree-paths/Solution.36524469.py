# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []

        paths = []
        self.get_all_paths(root, paths)
        return paths
        
    def get_all_paths(self, node, paths, cur=None):
        if cur is None:
            cur = []
            
        cur.append(node.val)
        
        try:
            if node.left is None and node.right is None:
                paths.append("->".join(str(n) for n in cur))
                return
                
            if node.left is not None:
                self.get_all_paths(node.left, paths, cur)
                
            if node.right is not None:
                self.get_all_paths(node.right, paths, cur)

        finally:
            cur.pop()
