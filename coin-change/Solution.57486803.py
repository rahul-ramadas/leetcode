class Solution:

    def coinChange(self, coins, amount):
        if amount <= 0:
            return 0

        seen = {0}
        boundary = {0}
        level = 0

        while boundary:
            level += 1
            boundary = {a + c for a in boundary for c in coins if not a + c in seen and a + c <= amount}
            if amount in boundary:
                return level

            seen.update(boundary)

        return -1
