class Solution(object):
    """Solution based on Pigeonhole principle."""

    def findDuplicate(self, nums):
        n = len(nums) - 1
        begin = 1
        end = n + 1

        while end - begin > 1:
            mid = (begin + end) / 2
            count_elems = len(filter(lambda x: begin <= x < mid, nums))
            max_possible = mid - begin
            if count_elems > max_possible:
                end = mid
            else:
                begin = mid

        return begin
