class Solution:

    def is_valid_bst(self, root, no_smaller_than, no_larger_than):
        if root is None:
            return True

        if no_smaller_than is not None and root.val <= no_smaller_than:
            return False

        if no_larger_than is not None and root.val >= no_larger_than:
            return False

        left_is_valid = self.is_valid_bst(root.left, no_smaller_than, root.val)
        if not left_is_valid:
            return False

        right_is_valid = self.is_valid_bst(root.right, root.val, no_larger_than)
        if not right_is_valid:
            return False

        return True

    def isValidBST(self, root):
        return self.is_valid_bst(root, None, None)
