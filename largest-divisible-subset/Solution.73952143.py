import unittest
import itertools
import random


class Solution:

    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] != 0:
                    continue

                if dp[j] + 1 > dp[i]:
                    prev[i] = j
                    dp[i] = dp[j] + 1

        largest_size = max(dp)
        index = dp.index(largest_size)
        solution = []
        while index != -1:
            solution.append(nums[index])
            index = prev[index]

        return solution


class TestSolution(unittest.TestCase):

    def is_valid_solution(self, nums):
        for i, j in itertools.combinations(nums, 2):
            if i % j != 0 and j % i != 0:
                return False
        return True

    def get_all_possible_solutions(self, nums):
        solutions = []

        for i in range(len(nums), 0, -1):
            for trial_set in itertools.combinations(nums, i):
                if not self.is_valid_solution(trial_set):
                    continue

                solutions.append(set(trial_set))

            if solutions:
                break

        return solutions

    def test_random_inputs(self):
        for trial in range(100):
            nums = random.sample(range(1, 51), 10)
            expected_solutions = self.get_all_possible_solutions(nums)
            actual = Solution().largestDivisibleSubset(nums)
            found = expected_solutions[0]
            for solution in expected_solutions:
                if set(actual) == solution:
                    found = solution
                    break
            self.assertSetEqual(set(actual), found)
