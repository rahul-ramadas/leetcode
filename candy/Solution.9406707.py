class Solution:

    def candy(self, ratings):
        if not ratings:
            return 0

        candies = 1
        incr = 1
        max_ind = 0
        max_candies = 1
        # assignment = [1]

        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                incr += 1
                candies += incr
                # assignment.append(incr)
                max_candies = incr
                max_ind = i
            elif ratings[i] == ratings[i - 1]:
                incr = 1
                max_candies = 1
                candies += incr
                # assignment.append(incr)
                max_ind = i
            else:   # ratings[i] < ratings[i - 1]
                incr = 1
                slope = i - (max_ind + 1)
                candies += 1 + slope
                # if slope:
                #     del assignment[-slope:]
                if slope + 1 == max_candies:
                    max_candies += 1
                    candies += 1
                    # assignment[-1] = max_candies
                # assignment.extend(range(slope + 1, 0, -1))

        # print(assignment)

        return candies
