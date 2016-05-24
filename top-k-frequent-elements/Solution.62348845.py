class Solution:

    def topKFrequent(self, nums, k):
        freq = collections.Counter(nums)
        buckets = [[] for _ in xrange(len(nums) + 1)]
        for num, freq in freq.items():
            buckets[freq].append(num)
        return list(itertools.islice(itertools.chain(*buckets[::-1]), k))
