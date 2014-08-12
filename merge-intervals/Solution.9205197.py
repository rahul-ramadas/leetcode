# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=operator.attrgetter('start'))
        result = []
        current_start = intervals[0].start
        current_end = intervals[0].end
        for i in intervals:
            if i.start <= current_end:
                current_end = max(current_end, i.end)
            else:
                result.append(Interval(current_start, current_end))
                current_start = i.start
                current_end = i.end
                
        result.append(Interval(current_start, current_end))
        
        return result
