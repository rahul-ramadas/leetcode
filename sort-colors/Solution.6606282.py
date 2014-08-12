class Solution:
    def sortColors(self, A):
        zeros = 0
        zerosOnes = 0
        zerosOnesTwos = 0

        for i in xrange(len(A)):
            if A[i] == 0:
                A[zerosOnesTwos] = 2
                A[zerosOnes] = 1
                A[zeros] = 0
                zerosOnesTwos += 1
                zerosOnes += 1
                zeros += 1
            elif A[i] == 1:
                A[zerosOnesTwos] = 2
                A[zerosOnes] = 1
                zerosOnesTwos += 1
                zerosOnes += 1
            elif A[i] == 2:
                A[zerosOnesTwos] = 2
                zerosOnesTwos += 1
