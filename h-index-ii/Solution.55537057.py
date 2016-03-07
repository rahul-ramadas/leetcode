class Solution:

    def hIndex(self, citations):
        if not citations:
            return 0

        n = len(citations)

        start = 0
        end = n
        while start < end:
            mid = (start + end) / 2
            count = n - mid
            at_least = citations[mid]
            if at_least == count:
                return count
            if count >= at_least:
                start = mid + 1
            elif count < at_least:
                end = mid

        return n - start
