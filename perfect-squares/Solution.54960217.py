class Solution:

    def numSquares(self, n):
        squares = [j * j for j in xrange(1, int(math.sqrt(n)) + 1)]

        cur_level = {0}
        next_level = set()
        visited = set()
        dist = 0

        while True:
            dist += 1
            next_level.update({num + sq for num in cur_level for sq in squares if num + sq not in visited and num + sq <= n})
            if n in next_level:
                return dist

            visited.update(next_level)

            cur_level = next_level
            next_level = set()

        # Unreachable. Lagrange's 4-square theorem proves that 4 is the maximum result.
