class Solution:

    def rob(self, root):
        return self.optimal_robbery(root, True)

    def optimal_robbery(self, root, can_rob_root):
        if root is None:
            return 0

        if can_rob_root and hasattr(root, "can_rob_root"):
            return root.can_rob_root
        if not can_rob_root and hasattr(root, "cannot_rob_root"):
            return root.cannot_rob_root

        self.compute_for_root(root)

        if can_rob_root:
            return root.can_rob_root
        else:
            return root.cannot_rob_root

    def compute_for_root(self, root):
        left_money = self.optimal_robbery(root.left, False)
        right_money = self.optimal_robbery(root.right, False)
        with_root = root.val + left_money + right_money

        left_money = self.optimal_robbery(root.left, True)
        right_money = self.optimal_robbery(root.right, True)
        without_root = left_money + right_money

        root.can_rob_root = max(with_root, without_root)
        root.cannot_rob_root = without_root
