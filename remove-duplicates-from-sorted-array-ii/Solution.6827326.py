class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0

        front = 0
        back = 0
        lastElement = A[0]
        lastElementCount = 0

        for front in xrange(len(A)):
            if A[front] != lastElement:
                A[back] = A[front]
                lastElement = A[front]
                lastElementCount = 1
                back += 1
            else:
                if lastElementCount != 2:
                    lastElementCount += 1
                    A[back] = A[front]
                    back += 1

        del A[back:]
        return back
