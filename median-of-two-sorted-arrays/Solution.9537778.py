class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        count = len(A) + len(B)
        if count % 2:
            k = count / 2 + 1
        else:
            k = count / 2

        low_a = 0
        high_a = len(A)
        low_b = 0
        high_b = len(B)

        while high_a - low_a and high_b - low_b:
            mid_a = (high_a + low_a) / 2
            mid_b = (high_b + low_b) / 2

            elems_a = (mid_a - low_a) + 1
            elems_b = (mid_b - low_b) + 1
            elems = elems_a + elems_b
            if A[mid_a] > B[mid_b]:
                if k < elems:
                    high_a = mid_a
                else:
                    low_b = mid_b + 1
                    k -= elems_b
            else:
                if k < elems:
                    high_b = mid_b
                else:
                    low_a = mid_a + 1
                    k -= elems_a

        if high_a - low_a:
            if count % 2:
                return A[low_a + k - 1]
            else:
                middle_one = A[low_a + k - 1]
                if low_b < len(B) and low_a + k < len(A):
                    middle_two = min(B[low_b], A[low_a + k])
                elif low_b < len(B):
                    middle_two = B[low_b]
                elif low_a + k < len(A):
                    middle_two = A[low_a + k]
                return (float(middle_one) + float(middle_two)) / 2.0
        else:
            if count % 2:
                return B[low_b + k - 1]
            else:
                middle_one = B[low_b + k - 1]
                if low_a < len(A) and low_b + k < len(B):
                    middle_two = min(A[low_a], B[low_b + k])
                elif low_a < len(A):
                    middle_two = A[low_a]
                elif low_b + k < len(B):
                    middle_two = B[low_b + k]
                return (float(middle_one) + float(middle_two)) / 2.0
