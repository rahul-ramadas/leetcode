import collections
import operator


class Solution:

    def majorityElement(self, num):
        counter = collections.Counter(num)
        return max(counter.items(), key=operator.itemgetter(1))[0]
