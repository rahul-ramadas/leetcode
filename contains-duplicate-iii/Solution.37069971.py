class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) < 2 or k < 1 or t < 0:
            return False
            
        bucket_size = t + 1
        buckets = {}
        
        for i, n in enumerate(nums):
            normal_n = n + sys.maxsize + 1
            bucket = normal_n / bucket_size
            
            if bucket in buckets:
                return True
                
            p_bucket = bucket - 1 
            if p_bucket in buckets and normal_n - buckets[p_bucket] <= t:
                return True
                
            n_bucket = bucket + 1
            if n_bucket in buckets and buckets[n_bucket] - normal_n <= t:
                return True
                
            if len(buckets) >= k:
                remove_n = nums[i - k] + sys.maxsize + 1
                remove_bucket = remove_n / bucket_size
                del buckets[remove_bucket]
                
            buckets[bucket] = normal_n
            
        return False
