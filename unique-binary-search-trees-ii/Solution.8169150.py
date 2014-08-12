class Solution:

    def get_list_of_trees_for_range(self, start, end):
        if start >= end:
            return [None]

        trees = []

        for i in xrange(start, end):
            for l in self.get_list_of_trees_for_range(start, i):
                for r in self.get_list_of_trees_for_range(i + 1, end):
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    trees.append(root)

        return trees

    def generateTrees(self, n):
        return self.get_list_of_trees_for_range(1, n + 1)
