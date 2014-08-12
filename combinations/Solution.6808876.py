class Solution:
    def combine(self, n, k):
        already_picked = [False] * n
        current_combination = [0] * k
        solution = []

        def pick_next_element(i, biggest_so_far):
            if i == k:
                solution.append(current_combination[:])
                return

            for j in xrange(biggest_so_far + 1, n):
                if already_picked[j]:
                    continue

                already_picked[j] = True
                current_combination[i] = j + 1
                pick_next_element(i + 1, j)
                already_picked[j] = False

        pick_next_element(0, -1)
        return solution
