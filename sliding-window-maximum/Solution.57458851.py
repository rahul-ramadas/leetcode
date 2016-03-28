class Solution:

    def maxSlidingWindow(self, nums, k):

        if not nums:
            return []

        candidates = []

        def add_to_candidate_list(candidates, window_start, num, index):
            while candidates and candidates[0][1] < window_start:
                del candidates[0]
            candidates[:] = [x for x in candidates[:] if x[0] > num]
            candidates.append((num, index))

        for i in xrange(k - 1):
            add_to_candidate_list(candidates, 0, nums[i], i)

        result = []
        for i in xrange(k - 1, len(nums)):
            add_to_candidate_list(candidates, i - (k - 1), nums[i], i)
            result.append(candidates[0][0])

        return result
