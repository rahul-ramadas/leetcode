class Solution:

    def maximumGap(self, num):
        n = len(num)
        if n < 2:
            return 0
        min_value = min(num)
        max_value = max(num)

        bucket_size = (max_value - min_value - 1) / (n - 1) + 1
        bucket_min_max = [(float('inf'), float('-inf'))] * n
        for x in num:
            index = (x - min_value) / bucket_size
            bucket_min_max[index] = (min(bucket_min_max[index][0], x), max(bucket_min_max[index][1], x))

        gap = 0
        last_max = bucket_min_max[0][1]
        for bucket_min, bucket_max in bucket_min_max[1:]:
            if bucket_min == float('inf'):
                continue
            gap = max(gap, bucket_min - last_max)
            last_max = bucket_max

        return gap
