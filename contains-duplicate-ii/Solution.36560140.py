class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        left = 0
        for right in range(len(nums)):
            if nums[right] in window:
                return True
                
            if k and len(window) == k:
                window.remove(nums[left])
                left += 1
                
            if k:
                window.add(nums[right])
            
        return False
