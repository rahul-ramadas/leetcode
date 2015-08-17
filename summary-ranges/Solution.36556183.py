class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
           
        seqs = [] 
        start = nums[0]
        
        for i in range(1, len(nums)):
            cur = nums[i]
            prev = nums[i - 1]
            
            if cur - prev > 1:
                if start == prev:
                    seq = "{}".format(start)
                else:
                    seq = "{}->{}".format(start, prev)
                seqs.append(seq)
                start = cur
                
        if start == nums[-1]:
            seq = "{}".format(start)
        else:
            seq = "{}->{}".format(start, nums[-1])
        seqs.append(seq)

        return seqs
