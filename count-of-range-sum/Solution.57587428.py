class Solution:

    def countRangeSum(self, nums, lower, upper):
        if not nums:
            return 0

        prefix_sums = [0] * len(nums)
        prefix_sums[0] = nums[0]
        for i in xrange(1, len(nums)):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i]

        def merge_sort_count(begin, end):
            if end - begin == 1:
                return 1 if lower <= prefix_sums[begin] <= upper else 0

            mid = (begin + end) / 2
            result = merge_sort_count(begin, mid) + merge_sort_count(mid, end)

            left = mid
            right = mid
            for i in xrange(begin, mid):
                while left < end and prefix_sums[left] - prefix_sums[i] < lower:
                    left += 1
                while right < end and prefix_sums[right] - prefix_sums[i] <= upper:
                    right += 1
                result += right - left

            prefix_sums[begin:end] = sorted(prefix_sums[begin:end])

            return result

        return merge_sort_count(0, len(prefix_sums))
