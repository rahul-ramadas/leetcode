class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []

        num.sort()
        result = []

        for i in xrange(len(num)):
            if i and num[i] == num[i - 1]:
                continue

            a = num[i]
            j = i + 1
            k = len(num) - 1
            target = -a
            while (j < k):
                b = num[j]
                c = num[k]
                sum = b + c
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    result.append([a, b, c])
                    j += 1
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                        
        return result
