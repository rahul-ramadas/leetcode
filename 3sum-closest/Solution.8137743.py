class Solution:

    def threeSumClosest(self, num, target):
        num = sorted(num)
        best_sum = num[0] + num[1] + num[2]

        for i in range(len(num)):
            j = i + 1
            k = len(num) - 1

            while j < k:
                current_sum = num[i] + num[j] + num[k]
                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(best_sum - target):
                    best_sum = current_sum

                if current_sum > target:
                    k -= 1
                else:
                    j += 1

        return best_sum
