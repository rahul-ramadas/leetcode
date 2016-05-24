class Solution(object):
    def intersect(self, nums1, nums2):
        nums1_counter = collections.Counter(nums1)
        nums2_counter = collections.Counter(nums2)
        
        result = []
        for k in nums1_counter.keys():
            if k in nums2_counter:
                result.extend([k] * min(nums1_counter[k], nums2_counter[k]))
        
        return result
