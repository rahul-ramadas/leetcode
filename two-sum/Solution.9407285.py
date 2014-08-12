class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        elems = list(enumerate(num, 1))
        elems.sort(key=operator.itemgetter(1))
        i = 0
        j = len(elems) - 1
        while i < j:
            trial = elems[i][1] + elems[j][1]
            if trial == target:
                return tuple(sorted((elems[i][0], elems[j][0])))
            elif trial > target:
                j -= 1
            else:   # trial < target
                i += 1
                
        return (-1, -1)
